"""Extract and convert .txt / .md files to structured Markdown.

Usage:
    python extract_txt.py <input_file> [--output-dir <dir>]
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import chardet
except ImportError:
    print("Error: chardet not installed. Run: pip install chardet")
    sys.exit(1)


def detect_encoding(filepath):
    with open(filepath, "rb") as f:
        raw = f.read()
    result = chardet.detect(raw)
    return result.get("encoding") or "utf-8", result.get("confidence", 1.0)


def extract_txt(filepath, output_dir):
    encoding, confidence = detect_encoding(filepath)
    print(f"[detect] encoding: {encoding}")

    if confidence < 0.7:
        print(f"[warn] low encoding confidence ({confidence:.0%}), content may have decoding errors")
    if encoding.lower() in ("gb2312", "gbk", "gb18030"):
        print(f"[warn] detected {encoding}, consider converting source file to UTF-8 for best results")

    with open(filepath, "r", encoding=encoding, errors="replace") as f:
        content = f.read()

    os.makedirs(output_dir, exist_ok=True)
    text_dir = os.path.join(output_dir, "text")
    os.makedirs(text_dir, exist_ok=True)

    raw_text_path = os.path.join(text_dir, "raw_text.txt")
    with open(raw_text_path, "w", encoding="utf-8") as f:
        f.write(content)

    extracted_path = os.path.join(output_dir, "extracted.md")
    with open(extracted_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[done] raw text: {raw_text_path}")
    print(f"[done] extracted: {extracted_path}")
    return extracted_path


def main():
    parser = argparse.ArgumentParser(description="Extract txt/md file to structured Markdown")
    parser.add_argument("input", help="Input .txt or .md file")
    parser.add_argument("--output-dir", "-o", default=None, help="Output directory (default: {input_name}/)")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"Error: file not found: {input_path}")
        sys.exit(1)

    output_dir = args.output_dir or str(input_path.parent / input_path.stem)

    try:
        extract_txt(str(input_path), output_dir)
    except Exception as e:
        print(f"Error: failed to process {input_path}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
