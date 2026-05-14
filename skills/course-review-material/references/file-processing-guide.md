# File Type Processing Guide

Detailed processing strategies for each supported file type.

## .txt / .md Files

| Aspect | Strategy |
|--------|----------|
| Encoding detection | Use `chardet` to detect and convert to UTF-8 |
| Text extraction | Read directly |
| Structure | Preserve original markdown headings; detect chapter/section boundaries |
| Images | N/A (no embedded images) |
| Output | Wrap in structured markdown with detected headings |

**Script template:** `scripts/extract_txt.py`

## .docx Files

| Aspect | Strategy |
|--------|----------|
| Library | `python-docx` |
| Text extraction | Traverse `document.paragraphs`, preserve `style.name` for heading detection |
| Images | Traverse paragraph XML for `w:drawing` elements, map `r:embed` to relationship part; save as PNG to `images/` |
| Tables | Convert `document.tables` to Markdown table format |
| Headings | Use built-in heading styles (Heading 1 → `#`, Heading 2 → `##`, etc.) |
| Lists | Detect list paragraphs via style name and `w:numPr`; use bullet format |
| Bold/Italic | Check `run.bold` / `run.italic` and wrap in `**` / `*` |

**Script template:** `scripts/extract_docx.py`

## .pptx Files

| Aspect | Strategy |
|--------|----------|
| Library | `python-pptx` |
| Slide text | Extract from all `shape.text_frame` on each slide |
| Slide images | Two sources: (a) embedded images in shapes, (b) render entire slide as PNG screenshot |
| Image priority | For image-only slides, render the full slide as PNG for recognition |
| Tables | Extract table shapes and convert to Markdown tables |
| Slide grouping | Use slide numbers; detect "section divider" slides for chapter boundaries |

**Script template:** `scripts/extract_pptx.py`

## .pdf Files

**Dual-layer strategy** — use both text extraction and image rendering:

| Layer | Library | Purpose |
|-------|---------|---------|
| Text layer | `pdfplumber` | Extract selectable text, tables, text positions |
| Image layer | `PyMuPDF (fitz)` | Render pages to PNG for visual/multimodal recognition |

**Processing flow:**
1. Open with `pdfplumber` → extract all text with page coordinates
2. If a page has significant text (>50 chars), trust the text layer
3. If a page has little or no text (<50 chars), flag as "image page" → render with `fitz` at 200 DPI → send to multimodal recognition
4. Extract embedded images via `fitz` for individual image recognition
5. Extract tables via `pdfplumber` table detection

**Script template:** `scripts/extract_pdf.py`
