"""Extract content from PDF files using dual-layer strategy.

Text layer: pdfplumber for selectable text and tables.
Image layer: PyMuPDF (fitz) for page rendering and embedded image extraction.

Usage:
    python extract_pdf.py <input.pdf> [--output-dir <dir>] [--dpi <dpi>] [--password <pwd>]
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("Error: pdfplumber not installed. Run: pip install pdfplumber")
    sys.exit(1)

try:
    import fitz
except ImportError:
    print("Error: PyMuPDF (fitz) not installed. Run: pip install PyMuPDF")
    sys.exit(1)


def extract_images_from_pdf_page(page, images_dir, page_num, img_counter):
    image_refs = []
    image_list = page.get_images(full=True)

    for img_idx, img_info in enumerate(image_list):
        xref = img_info[0]
        base_image = page.parent.extract_image(xref)
        ext = base_image["ext"]
        img_name = f"img_{img_counter + 1:03d}.{ext}"
        img_path = os.path.join(images_dir, img_name)
        with open(img_path, "wb") as f:
            f.write(base_image["image"])
        image_refs.append(img_name)
        img_counter += 1

    return image_refs, img_counter


def render_page_to_png(doc, page_num, pages_dir, dpi=200):
    page = doc[page_num]
    mat = fitz.Matrix(dpi / 72, dpi / 72)
    pix = page.get_pixmap(matrix=mat)
    page_path = os.path.join(pages_dir, f"page_{page_num + 1:03d}.png")
    pix.save(page_path)
    return page_path


def extract_table_as_md(table):
    rows = table
    if not rows:
        return ""

    header = rows[0]
    if header is None:
        return ""

    md_lines = []
    md_lines.append("| " + " | ".join(str(c) or "" for c in header) + " |")
    md_lines.append("| " + " | ".join(["---"] * len(header)) + " |")
    for row in rows[1:]:
        if row:
            padded = list(row) + [""] * (len(header) - len(row))
            md_lines.append("| " + " | ".join(str(c) or "" for c in padded[:len(header)]) + " |")

    return "\n".join(md_lines)


def extract_pdf(filepath, output_dir, dpi=200, password=None):
    os.makedirs(output_dir, exist_ok=True)

    text_dir = os.path.join(output_dir, "text")
    images_dir = os.path.join(output_dir, "images")
    pages_dir = os.path.join(output_dir, "pages")
    os.makedirs(text_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(pages_dir, exist_ok=True)

    md_lines = []
    raw_texts = []
    img_counter = 0
    image_page_count = 0

    fitz_doc = fitz.open(filepath)
    if password:
        if fitz_doc.authenticate(password) == 0:
            print("Error: incorrect PDF password")
            fitz_doc.close()
            sys.exit(1)

    with pdfplumber.open(filepath, password=password) as pdf:
        for page_num, page in enumerate(pdf.pages):
            page_header = f"\n## Page {page_num + 1}\n"
            md_lines.append(page_header)

            text = page.extract_text()
            if text:
                text_len = len(text.strip())
            else:
                text_len = 0

            if text_len > 50:
                md_lines.append(text + "\n")
                raw_texts.append(text)

                tables = page.extract_tables()
                for table in tables:
                    if table:
                        md_lines.append("\n" + extract_table_as_md(table) + "\n")

            else:
                image_page_count += 1
                png_path = render_page_to_png(fitz_doc, page_num, pages_dir, dpi)
                rel_path = os.path.relpath(png_path, output_dir)
                md_lines.append(f"![Page {page_num + 1}]({rel_path})\n")
                md_lines.append(f"<!-- page source: page_{page_num + 1:03d}.png (needs multimodal recognition) -->\n")

            fitz_page = fitz_doc[page_num]
            image_refs, img_counter = extract_images_from_pdf_page(
                fitz_page, images_dir, page_num, img_counter
            )
            for img_ref in image_refs:
                md_lines.append(f"![Embedded image](images/{img_ref})\n")
                md_lines.append(f"<!-- image source: {img_ref} -->\n")

    total_pages = len(fitz_doc)
    fitz_doc.close()

    raw_text_path = os.path.join(text_dir, "raw_text.txt")
    with open(raw_text_path, "w", encoding="utf-8") as f:
        f.write("\n".join(raw_texts))

    extracted_path = os.path.join(output_dir, "extracted.md")
    with open(extracted_path, "w", encoding="utf-8") as f:
        f.write("".join(md_lines))

    print(f"[done] total pages: {total_pages}")
    print(f"[done] image-only pages (needs recognition): {image_page_count}")
    print(f"[done] embedded images extracted: {img_counter}")
    print(f"[done] raw text: {raw_text_path}")
    print(f"[done] extracted: {extracted_path}")
    return extracted_path


def main():
    parser = argparse.ArgumentParser(description="Extract PDF content to structured Markdown")
    parser.add_argument("input", help="Input .pdf file")
    parser.add_argument("--output-dir", "-o", default=None, help="Output directory (default: {input_name}/)")
    parser.add_argument("--dpi", type=int, default=200, help="DPI for page rendering (default: 200)")
    parser.add_argument("--password", "-p", default=None, help="PDF password if encrypted")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"Error: file not found: {input_path}")
        sys.exit(1)

    output_dir = args.output_dir or str(input_path.parent / input_path.stem)

    try:
        extract_pdf(str(input_path), output_dir, dpi=args.dpi, password=args.password)
    except Exception as e:
        print(f"Error: failed to process {input_path}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
