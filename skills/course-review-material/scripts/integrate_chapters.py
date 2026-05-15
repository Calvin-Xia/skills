"""Integrate per-file extracted.md files into chapter-organized review notes.

Reads course-config.yaml, loads all extracted.md files, matches content
to chapters, deduplicates, and outputs chapter-split markdown files.

Usage:
    python integrate_chapters.py <course-config.yaml> [--output-dir <dir>]
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install PyYAML")
    sys.exit(1)


def load_config(config_path):
    config_path = Path(config_path).resolve()
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    for ch in config.get("chapters", []):
        ch["id"] = int(ch["id"])

    config["_config_dir"] = str(config_path.parent)
    return config


def load_extracted_content(config):
    all_blocks = []
    config_dir = Path(config["_config_dir"])

    for file_entry in config.get("files", []):
        file_path = config_dir / file_entry["path"]
        extracted_md = _find_extracted_md(file_path, config_dir, file_entry)

        if not extracted_md.exists():
            print(f"[warn] extracted.md not found for {file_entry['path']} at {extracted_md}")
            continue

        with open(extracted_md, "r", encoding="utf-8") as f:
            content = f.read()

        blocks = split_into_blocks(content, file_entry.get("label", file_entry["path"]))
        all_blocks.extend(blocks)
        print(f"[load] {file_entry['path']}: {len(blocks)} content blocks")

    return all_blocks


def _find_extracted_md(file_path, config_dir, file_entry):
    extracted_md = file_path.parent / file_path.stem / "extracted.md"
    if extracted_md.exists():
        return extracted_md

    stem = file_path.stem
    alt_name = file_path.parent / stem / "extracted.md"
    if alt_name != extracted_md and alt_name.exists():
        return alt_name

    config_adjacent = config_dir / file_path.name
    candidate = config_adjacent.parent / config_adjacent.stem / "extracted.md"
    if candidate.exists():
        return candidate

    return extracted_md


def split_into_blocks(content, source_label):
    blocks = []
    current_section = ""
    current_content = []
    lines = content.split("\n")

    section_pattern = re.compile(r"^#{1,3}\s+")

    for line in lines:
        if section_pattern.match(line):
            if current_content:
                blocks.append({
                    "section": current_section,
                    "content": "\n".join(current_content).strip(),
                    "source": source_label,
                })
            current_section = line
            current_content = [line]
        else:
            current_content.append(line)

    if current_content:
        blocks.append({
            "section": current_section,
            "content": "\n".join(current_content).strip(),
            "source": source_label,
        })

    merged_blocks = []
    current = None
    for block in blocks:
        if current and current["section"] and not block["section"]:
            current["content"] += "\n" + block["content"]
        else:
            if current:
                merged_blocks.append(current)
            current = block
    if current:
        merged_blocks.append(current)

    return merged_blocks


def match_block_to_chapter(block, chapters):
    content = block.get("content", "")
    section = block.get("section", "")

    for chapter in chapters:
        for pattern in chapter.get("match_patterns", []):
            try:
                if re.search(pattern, content) or re.search(pattern, section):
                    return chapter["id"]
            except re.error:
                if pattern in content or pattern in section:
                    return chapter["id"]

        for keyword in chapter.get("keywords", []):
            if keyword in content:
                return chapter["id"]

    title_parts = section.lstrip("#").strip()
    for chapter in chapters:
        if chapter["title"] and chapter["title"] in title_parts:
            return chapter["id"]

    return None


def assign_chapters(blocks, chapters):
    chapter_blocks = defaultdict(list)
    unassigned = []

    for block in blocks:
        chapter_id = match_block_to_chapter(block, chapters)
        if chapter_id:
            chapter_blocks[chapter_id].append(block)
        else:
            unassigned.append(block)

    return chapter_blocks, unassigned


def deduplicate_blocks(blocks):
    if not blocks:
        return blocks

    deduplicated = [blocks[0]]
    possible_dup_count = 0

    for block in blocks[1:]:
        is_dup = False
        is_possible = False
        for existing in deduplicated:
            ratio = SequenceMatcher(
                None,
                block["content"].replace("\n", " ").strip(),
                existing["content"].replace("\n", " ").strip(),
            ).ratio()
            if ratio > 0.95:
                is_dup = True
                existing.setdefault("sources", [existing["source"]])
                if block["source"] not in existing["sources"]:
                    existing["sources"].append(block["source"])
                break
            elif ratio > 0.85:
                is_possible = True

        if is_dup:
            continue

        if is_possible:
            block["_possible_dup"] = True
            possible_dup_count += 1

        deduplicated.append(block)

    if possible_dup_count:
        print(f"[dedup] {possible_dup_count} possible duplicates (85%-95% similarity) kept for review")

    return deduplicated


def write_chapter_file(chapter, blocks, output_dir, config):
    os.makedirs(output_dir, exist_ok=True)

    ch_id = chapter["id"]
    ch_title = chapter["title"] or f"Chapter {ch_id}"
    safe_title = re.sub(r'[\\/:*?"<>|]', "-", ch_title)
    filename = f"ch{ch_id:02d}-{safe_title}.md"
    filepath = os.path.join(output_dir, filename)

    lines = []
    lines.append(f"# 第{ch_id}章 {ch_title}\n")

    course_name = config.get("course", {}).get("name", "")
    sources = sorted(set(b.get("source", "") for b in blocks))
    keywords = chapter.get("keywords", [])

    if course_name:
        lines.append(f"> **课程**: {course_name}\n")
    if sources:
        lines.append(f"> **来源**: {', '.join(sources)}\n")
    if keywords:
        lines.append(f"> **关键词**: {', '.join(keywords)}\n")

    lines.append("\n---\n")

    for block in blocks:
        content = block["content"]
        source_note = block.get("source", "")

        if source_note and source_note not in content:
            content = f"<!-- source: {source_note} -->\n" + content

        lines.append(content + "\n")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[write] {filepath} ({len(blocks)} blocks)")
    return filepath


def write_index(output_dir, chapters, chapter_files, config, unassigned_path=None):
    filepath = os.path.join(output_dir, "index.md")
    lines = []

    course_name = config.get("course", {}).get("name", "课程复习资料")
    lines.append(f"# {course_name} - 复习资料目录\n")

    semester = config.get("course", {}).get("semester", "")
    instructor = config.get("course", {}).get("instructor", "")
    file_labels = [f.get("label", f.get("path", "")) for f in config.get("files", [])]

    meta = []
    if semester:
        meta.append(f"**学期**: {semester}")
    if instructor:
        meta.append(f"**教师**: {instructor}")
    meta.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    if file_labels:
        meta.append(f"**源文件**: {', '.join(file_labels)}")

    lines.append("> " + "  \n> ".join(meta) + "\n")
    lines.append("## 目录\n")

    for chapter in chapters:
        ch_id = chapter["id"]
        ch_title = chapter["title"] or f"Chapter {ch_id}"
        safe_title = re.sub(r'[\\/:*?"<>|]', "-", ch_title)
        ch_filename = f"ch{ch_id:02d}-{safe_title}.md"
        lines.append(f"| 第{ch_id}章 {ch_title} | [{ch_filename}]({ch_filename}) |")

    lines.append("")

    if unassigned_path:
        lines.append("## 未分类内容\n")
        lines.append(f"[未分类内容.md]({os.path.basename(unassigned_path)})\n")

    lines.append("## 附录\n")
    lines.append("### 原始文件提取结果\n")

    config_dir = Path(config["_config_dir"])
    for file_entry in config.get("files", []):
        file_path = config_dir / file_entry["path"]
        extracted_md = file_path.parent / file_path.stem / "extracted.md"
        try:
            rel_path = os.path.relpath(extracted_md, output_dir)
        except ValueError:
            rel_path = str(extracted_md)
        lines.append(f"| {file_entry.get('label', file_entry['path'])} | [{rel_path}]({rel_path}) |")

    lines.append("")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[write] {filepath}")
    return filepath


def write_unassigned(unassigned_blocks, output_dir):
    if not unassigned_blocks:
        return None

    filepath = os.path.join(output_dir, "未分类内容.md")
    lines = ["# 未分类内容\n"]
    lines.append("> 以下内容未能自动匹配到任何章节，请手动归类。\n\n---\n")

    for block in unassigned_blocks:
        source_note = block.get("source", "")
        content = block["content"]
        if source_note and source_note not in content:
            content = f"<!-- source: {source_note} -->\n" + content
        lines.append(content + "\n---\n")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[write] {filepath} ({len(unassigned_blocks)} unassigned blocks)")
    return filepath


def integrate(config_path, output_dir=None):
    config = load_config(config_path)

    chapters = config.get("chapters", [])
    if not chapters:
        print("Error: no chapters defined in config")
        sys.exit(1)

    output_dir = output_dir or config.get("output", {}).get("integrated_dir", "review-notes")
    config_dir = Path(config["_config_dir"])
    if not os.path.isabs(output_dir):
        output_dir = str(config_dir / output_dir)

    print(f"[start] loading extracted content...")
    all_blocks = load_extracted_content(config)

    print(f"\n[assign] matching {len(all_blocks)} blocks to {len(chapters)} chapters...")
    chapter_blocks, unassigned = assign_chapters(all_blocks, chapters)

    print(f"\n[dedup] removing duplicates...")
    for ch_id in chapter_blocks:
        before = len(chapter_blocks[ch_id])
        chapter_blocks[ch_id] = deduplicate_blocks(chapter_blocks[ch_id])
        after = len(chapter_blocks[ch_id])
        if before != after:
            print(f"  Chapter {ch_id}: {before} → {after} blocks ({before - after} duplicates removed)")

    print(f"\n[write] generating chapter files...")
    chapter_files = []
    chapter_map = {ch["id"]: ch for ch in chapters}
    for ch_id, blocks in sorted(chapter_blocks.items()):
        chapter = chapter_map.get(ch_id, {"id": ch_id, "title": f"Chapter {ch_id}", "keywords": []})
        ch_file = write_chapter_file(chapter, blocks, output_dir, config)
        chapter_files.append(ch_file)

    unassigned_file = None
    if unassigned:
        print(f"\n[write] {len(unassigned)} unassigned blocks → 未分类内容.md")
        unassigned_file = write_unassigned(unassigned, output_dir)

    print(f"\n[write] generating index...")
    write_index(output_dir, chapters, chapter_files, config, unassigned_file)

    print(f"\n=== Integration Complete ===")
    print(f"  Chapters: {len(chapter_files)} files")
    print(f"  Unassigned: {len(unassigned)} blocks")
    print(f"  Output: {output_dir}")

    for ch in chapters:
        ch_id = ch["id"]
        if ch_id in chapter_blocks:
            count = len(chapter_blocks[ch_id])
            print(f"    Ch{ch_id:02d} {ch['title']}: {count} blocks")
        else:
            print(f"    Ch{ch_id:02d} {ch['title']}: (empty)")

    if unassigned:
        print(f"    ⚠  {len(unassigned)} unassigned blocks → review 未分类内容.md")


def main():
    parser = argparse.ArgumentParser(description="Integrate extracted content into chapter-organized review notes")
    parser.add_argument("config", help="Path to course-config.yaml")
    parser.add_argument("--output-dir", "-o", default=None, help="Output directory for chapter files")
    args = parser.parse_args()

    config_path = Path(args.config).resolve()
    if not config_path.exists():
        print(f"Error: config file not found: {config_path}")
        sys.exit(1)

    try:
        integrate(str(config_path), output_dir=args.output_dir)
    except Exception as e:
        print(f"Error: integration failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
