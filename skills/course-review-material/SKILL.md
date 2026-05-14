---
name: course-review-material
description: Use when a college student needs to parse course lecture materials
  (docx, pptx, pdf, txt) and organize them into structured chapter-by-chapter
  Markdown review notes for exam preparation. Triggers: "整理复习资料",
  "parse course materials", "extract lecture content", "organize study notes
  from slides", "复习资料生成", "课程复习", "期末复习", "开卷考试资料整理".
---

# Course Review Material Generator

## Overview

Parse course materials into structured chapter-organized Markdown review notes. **Core principle**: Preserve original text verbatim — no paraphrasing, no rewriting.

## When to Use

```
User mentions "复习" or "整理" with course files?
├── Files are docx/pptx/pdf/txt? → Use this skill
├── Need chapter-organized output? → Use this skill
├── Just need a single file converted? → Use this skill (still useful)
└── Need to edit or annotate content? → NOT this skill (use docx/pdf skills directly)
```

**Use this skill when:**
- User has course materials (docx/pptx/pdf/txt) and wants structured review notes
- Materials contain mixtures of text, embedded images, formulas, tables, or code
- User needs chapter-by-chapter organization for exam preparation
- Multiple files from the same course need consolidation into unified notes
- Images in slides/docs need content recognition (formulas, charts, text in images)

**Do NOT use when:**
- User only wants format conversion without content organization
- User needs to edit the original files
- Content is already perfectly structured and just needs minor formatting

## Environment Check (MANDATORY FIRST STEP)

1. **Python libraries**: Run `pip install python-docx python-pptx pdfplumber PyMuPDF Pillow PyYAML chardet` if any are missing. Verify with:
   `python -c "import docx, pptx, pdfplumber, fitz, PIL, yaml, chardet; print('OK')"`

2. **Multimodal capability**: Required for image recognition (formulas, diagrams, embedded text in images).
   - **Available** (Claude Vision, GPT-4V, etc.): Use for all image tasks.
   - **Not available**: Display warning and fall back to local OCR (`pip install pytesseract paddleocr`).
     > ⚠️ No multimodal model detected. Using local OCR fallback — formula recognition will be limited.

## Workflow: Two-Phase Processing

### Phase 1: Per-File Content Extraction

Extract content from each source file independently. Produce structured Markdown and save intermediate artifacts.

```
Source File → Parse → Extract text/images → Multimodal recognition → extracted.md
```

**For each file, produce:** `{source_name}/` with `text/`, `images/`, `recognized/` dirs and an `extracted.md`. See Directory Structure Convention for full layout.

### Phase 2: Cross-File Integration

Merge all `extracted.md` files into chapter-organized review notes using the YAML chapter configuration.

```
All extracted.md + course-config.yaml → Chapter matching → Merge & dedup → Chapter files + index.md
```

**Output structure:**
```
{integrated_dir}/
├── index.md            # Table of contents with links
├── ch01-{title}.md     # Chapter 1
├── ch02-{title}.md     # Chapter 2
└── ...
```

## File Type Processing

| Type | Library | Script | Key Strategy |
|------|---------|--------|--------------|
| .txt/.md | chardet | `scripts/extract_txt.py` | Detect encoding, preserve structure |
| .docx | python-docx | `scripts/extract_docx.py` | Preserve styles, extract images |
| .pptx | python-pptx | `scripts/extract_pptx.py` | Extract text + render slides |
| .pdf | pdfplumber + PyMuPDF | `scripts/extract_pdf.py` | Dual-layer: text + image rendering |

For detailed processing strategies per file type, see **[references/file-processing-guide.md](references/file-processing-guide.md)**.

## Content Type Handling

### Text Content

```
Rule: PRESERVE ORIGINAL TEXT VERBATIM. Do not paraphrase or rewrite.
```

- Keep the teacher's exact phrasing, examples, and explanations
- Apply heading hierarchy based on document structure or chapter config
- Preserve bold (`**text**`), italic (`*text*`), and list formatting
- Use blockquotes (`>`) for highlighted/boxed key points from slides

### Image Content

```
Decision Tree:
├── Multimodal model available?
│   ├── YES → Send image to model with prompt: "Describe this image in detail.
│   │         If it contains formulas, output them as LaTeX. If it contains text,
│   │         transcribe it. If it's a diagram, describe its structure and labels."
│   │         → Inline the recognized content into markdown
│   └── NO → Fall back to local OCR (pytesseract/PaddleOCR)
│             → Inline recognized text, flag low-confidence results
└── Recognition fails or image is purely decorative?
    └── Use GFM format: ![description](images/img_001.png)
```

**Image recognition prompt template (for multimodal models):**

```
Analyze this image from course materials. Output requirements:
1. If it contains mathematical formulas → output them as LaTeX ($...$ or $$...$$)
2. If it contains text → transcribe the text exactly
3. If it's a diagram/chart → describe the structure, labels, and key information
4. If it's a photo/illustration → describe what it shows in one sentence
5. Always start with a concise label like **[Figure: xxx]** or **[Formula]** or **[Table]**
```

**Annotation:** Each inline recognition result must be annotated with its source:
```markdown
<!-- image source: img_001.png -->
```

### Formulas

```
Rule: ALL formulas MUST be converted to LaTeX. No formula screenshots.
```

| Scenario | Action |
|----------|--------|
| Text already contains LaTeX (`$...$`) | Preserve as-is |
| Text contains plain-text formula (`E=mc^2`) | Wrap in `$...$` |
| Formula in image | Multimodal model → output LaTeX |
| Complex formula that cannot be expressed in LaTeX | Fallback: `![Formula](images/formula_001.png)` |
| Chemical equations | Use plain text or `\ce{...}` if mhchem is available |

**Common LaTeX patterns in Chinese course materials:**
- Fractions: `\frac{分子}{分母}`
- Limits: `\lim_{x \to 0}`
- Integrals: `\int_{a}^{b}`
- Summation: `\sum_{i=1}^{n}`
- Matrices: `\begin{pmatrix} ... \end{pmatrix}`

### Code and Algorithms

- Wrap code blocks with language tag: ` ```python ... ``` `
- Pseudo-code: use ` ```text ``` ` or ` ```algorithm ``` `
- Preserve indentation exactly
- Add brief context comment if the code purpose is unclear from surrounding text

### Tables

Convert all tables to Markdown table format:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| cell 1   | cell 2   | cell 3   |
```

For wide tables, note if the table is truncated and suggest the user review the original.

## Chapter Detection Heuristics

Chapter detection is a critical step. Use this priority order:

### Priority 1: YAML Configuration (most reliable)

Match content against `chapters[].match_patterns` in `course-config.yaml`. Each pattern can be:
- Exact string match: `"第一章 函数与极限"`
- Regex pattern: `"第[一1]章"`
- Keyword presence: matched against `chapters[].keywords`

### Priority 2: Standard Heading Styles

- **docx**: Paragraphs with `style.name` matching `'Heading 1'`, `'Heading 2'`, etc.
- **pptx**: Slides with title placeholders or largest font size + bold text
- **pdf**: Text with largest font size on a page (from `pdfplumber` char analysis)
- **txt/md**: Lines matching `^#+\s+` markdown heading pattern

### Priority 3: Numbering Patterns

Detect common Chinese academic numbering:
- `第一章`, `第二章`, ... → Chapter
- `第1章`, `第2章`, ... → Chapter
- `§1`, `§2`, ... → Chapter/section
- `一、`, `二、`, ... → Section (under a chapter)
- `1.1`, `1.2`, ... → Subsection
- `Chapter 1`, `Ch. 1` → Chapter (English)

### Priority 4: Font Size Mutation

When no structural clues exist:
- Text with font size ≥ 18pt and bold → potential chapter heading
- Text with font size ≥ 14pt and bold → potential section heading
- Compare against median body text size to detect outliers

### Priority 5: Fallback

Content that cannot be assigned to any chapter → mark as `## 未分类内容` (Unclassified Content) and prompt user to specify chapter manually.

## YAML Configuration

Use the template in **[config_template.yaml](config_template.yaml)**. Generate interactively:
1. Ask for course name, semester, instructor
2. Ask for all source file paths → auto-detect types from extensions
3. Ask for chapter list (number + titles)
4. Ask for optional keywords per chapter
5. Generate `course-config.yaml` and **confirm with user** before proceeding

## Directory Structure Convention

```
课程资料目录/
├── {源文件1}.docx                  # Original source file
├── {源文件1}/                      # Process artifacts (same name as source)
│   ├── images/                    # Extracted images
│   │   └── recognized/            # Multimodal/OCR recognition results
│   ├── text/                      # Raw text extraction
│   └── extracted.md               # Structured extraction (Final Product 1)
├── {源文件2}.pptx
├── {源文件2}/
│   ├── slides/                    # Rendered slide screenshots
│   ├── images/
│   └── extracted.md
├── course-config.yaml             # User configuration
└── review-notes/                  # Final Product 2: Integrated review notes
    ├── index.md                   # Master table of contents
    ├── ch01-{章节名}.md
    ├── ch02-{章节名}.md
    └── ...
```

### Naming Conventions

- Process artifact directory: **exact same name as source file** (without extension for PPT batch)
- Chapter files: `ch{02d}-{title}.md` (zero-padded, two-digit chapter ID)
- Image files: `img_{03d}.png` (zero-padded, sequential)
- Slide files: `slide_{03d}.png` (zero-padded, matching slide number)

## Output Format

Each chapter file follows the structure in **[assets/output-templates.md](assets/output-templates.md)**. Key requirements:
- Chapter header with source annotations and keywords
- Section-level organization matching the YAML config
- Inline image recognition results annotated with `<!-- image source: ... -->`
- All formulas converted to LaTeX

The index file (`index.md`) provides a master table of contents linking to all chapter files.

## Cross-File Deduplication

When merging multiple source files into chapters:

1. **Exact match**: If two paragraphs are identical (after normalizing whitespace), keep only one, note the sources.
2. **Near-duplicate** (>80% similarity via `difflib.SequenceMatcher`): Keep the more complete version, note the other source.
3. **Complementary content**: If two files cover the same topic differently, merge with source annotations:

```markdown
> **讲义补充**: {补充内容}

> **PPT要点**: {PPT中的要点}
```

4. **Conflict**: If two files contradict, keep both with a conflict marker:

```markdown
> ⚠️ **内容不一致**:
> - 讲义: {版本A}
> - PPT: {版本B}
```

## Quick Reference

| Task | Command / Approach |
|------|-------------------|
| Install all deps | `pip install python-docx python-pptx pdfplumber PyMuPDF Pillow PyYAML chardet` |
| Detect file encoding | `chardet.detect(open(f, 'rb').read())` |
| Extract docx text | `python scripts/extract_docx.py <file.docx>` |
| Extract pptx text | `python scripts/extract_pptx.py <file.pptx>` |
| Extract pdf text | `python scripts/extract_pdf.py <file.pdf>` |
| Integrate chapters | `python scripts/integrate_chapters.py course-config.yaml` |
| Test multimodal availability | Send a test image and check if description is returned |
| Check PDF text vs image | If `len(page.extract_text()) < 50` → treat as image page |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Skipping image-only PDF pages | Image-only pages often contain critical content (formulas, diagrams). Always run multimodal recognition. |
| Using screenshots for formulas | Convert formulas to LaTeX. Searchable, copyable, uniform formatting. |
| Forcing all content into one file | Split by chapter. Single large files are harder to navigate during open-book exams. |
| Rewriting teacher's text | Preserve original text. The purpose is faithful extraction, not summarization. |
| Not asking for chapter config | Always generate `course-config.yaml` interactively before extraction. Without it, chapter assignment is guesswork. |
| Omitting source annotations | Every extracted/reorganized block should note which file it came from. |
| Using absolute paths in markdown links | Use relative paths. The notes should be portable. |

## STOP Signs

These are **hard stops** — when you encounter them, you MUST take the specified action and not proceed otherwise:

| STOP Sign | Required Action |
|-----------|----------------|
| 🔴 Pure image PDF/PPT (no text layer at all) | MUST run multimodal recognition on every page. Do not skip or mark as "empty". |
| 🔴 Formula encountered in any form | MUST attempt LaTeX conversion. Do not screenshot. |
| 🔴 User says "随便整整" (just roughly organize) | MUST ask for chapter structure. Random organization defeats the purpose. |
| 🔴 Content cannot be assigned to any chapter | MUST mark as `## 未分类内容` and ask user where it belongs. Do not guess. |
| 🔴 No `course-config.yaml` exists | MUST generate it interactively before starting extraction. |
| 🔴 Encrypted/protected file | MUST ask user for password or to decrypt first. Do not skip. |

## Rationalization Counter-Table

When you catch yourself thinking these thoughts, read the reality:

| Excuse | Reality |
|--------|---------|
| "这个PDF看起来没有文字，跳过就行了" | 纯图片型PDF正是需要多模态识别的场景，跳过等于丢弃所有内容。 |
| "公式直接用截图放进去就好" | LaTeX可搜索、可复制、排版统一，复习效率远高于截图。 |
| "章节就是从一级标题来的" | 老师PPT可能用特大号字+加粗而非标准标题样式，必须结合config多策略检测。 |
| "所有内容放一个md文件就行了" | 按章节分文件是用户明确需求，分文件便于阶段性复习和开卷考试快速定位。 |
| "图片懒得识别了，跳过吧" | 图片中的公式/图表/文字可能是考点，必须识别。识别失败才用GFM引用。 |
| "这个表格太复杂，截图吧" | 表格应转Markdown table格式，保持结构化。实在无法转换才保留截图。 |
| "内容差不多，合并到一起吧" | 必须标注来源。讲义和PPT可能有细微差异（都是考点）。 |
| "用户应该自己知道章节" | 主动引导用户填写config，不要等待用户提供。 |

## Red Flags — STOP and Review

- [ ] You're about to skip an image without recognition attempt
- [ ] You're about to paste a formula as an image
- [ ] You're about to dump all content into one file
- [ ] You're processing without `course-config.yaml`
- [ ] You're paraphrasing instead of preserving original text
- [ ] You're guessing chapter assignment without asking user

**Any checkbox checked means: stop, fix the issue, then continue.**

## Edge Cases

1. **Encrypted PDF**: Prompt user: "此PDF文件已加密，请提供密码或先解密后再处理。"
2. **Very large files (>100 pages)**: Process in batches of 20 pages. Show progress: "正在处理第 X-Y 页 / 共 Z 页..."
3. **Poor quality scans**: If OCR confidence < 60%, mark result with `[识别置信度低]` and keep original image reference.
4. **Mixed languages**: Detect via `langdetect` or similar. Use `output.language` from config as primary; mark other-language sections.
5. **Broken/missing fonts in PDF**: This is common with Chinese PDFs. Render as image and use multimodal recognition as fallback.
6. **PPT with animations**: `python-pptx` can only access static content. Warn user if animations might hide content.
7. **Duplicate slides in PPT**: Some PPTs have build slides (same content, incremental reveals). Keep only the most complete version (last slide in a build sequence).

## Script Reference

The `scripts/` directory contains executable Python templates for each file type:

- **[scripts/extract_txt.py](scripts/extract_txt.py)** — Text/markdown file extraction
- **[scripts/extract_docx.py](scripts/extract_docx.py)** — Word document extraction with image export
- **[scripts/extract_pptx.py](scripts/extract_pptx.py)** — PowerPoint extraction with slide rendering
- **[scripts/extract_pdf.py](scripts/extract_pdf.py)** — PDF dual-layer extraction (text + image)
- **[scripts/integrate_chapters.py](scripts/integrate_chapters.py)** — Cross-file chapter integration and deduplication

Also see **[config_template.yaml](config_template.yaml)** for the YAML configuration template.
