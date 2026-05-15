# Content Type Handling Reference

Detailed processing strategies for each content type encountered in course materials.

## Text Content

**Rule: PRESERVE ORIGINAL TEXT VERBATIM. Do not paraphrase or rewrite.**

- Keep the teacher's exact phrasing, examples, and explanations
- Apply heading hierarchy based on document structure or chapter config
- Preserve bold (`**text**`), italic (`*text*`), and list formatting
- Use blockquotes (`>`) for highlighted/boxed key points from slides

## Image Content

**Decision Tree:**
- Multimodal model available?
  - YES: Send image to model with prompt: "Describe this image in detail. If it contains formulas, output them as LaTeX. If it contains text, transcribe it. If it's a diagram, describe its structure and labels." → Inline the recognized content into markdown
  - NO: Fall back to local OCR (pytesseract/PaddleOCR) → Inline recognized text, flag low-confidence results
- Recognition fails or image is purely decorative? → Use GFM format: `![description](images/img_001.png)`

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

## Formulas

**Rule: ALL formulas MUST be converted to LaTeX. No formula screenshots.**

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

## Code and Algorithms

- Wrap code blocks with language tag: ` ```python ... ``` `
- Pseudo-code: use ` ```text ``` ` or ` ```algorithm ``` `
- Preserve indentation exactly
- Add brief context comment if the code purpose is unclear from surrounding text

## Tables

Convert all tables to Markdown table format:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| cell 1   | cell 2   | cell 3   |
```

For wide tables, note if the table is truncated and suggest the user review the original.
