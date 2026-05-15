# Chapter Detection Heuristics

Chapter detection is critical for organizing extracted content. Use these strategies in priority order.

## Priority 1: YAML Configuration (most reliable)

Match content against `chapters[].match_patterns` in `course-config.yaml`. Each pattern can be:
- Exact string match: `"第一章 函数与极限"`
- Regex pattern: `"第[一1]章"`
- Keyword presence: matched against `chapters[].keywords`

## Priority 2: Standard Heading Styles

- **docx**: Paragraphs with `style.name` matching `'Heading 1'`, `'Heading 2'`, etc.
- **pptx**: Slides with title placeholders or largest font size + bold text
- **pdf**: Text with largest font size on a page (from `pdfplumber` char analysis)
- **txt/md**: Lines matching `^#+\s+` markdown heading pattern

## Priority 3: Numbering Patterns

Detect common Chinese academic numbering:
- `第一章`, `第二章`, ... → Chapter
- `第1章`, `第2章`, ... → Chapter
- `§1`, `§2`, ... → Chapter/section
- `一、`, `二、`, ... → Section (under a chapter)
- `1.1`, `1.2`, ... → Subsection
- `Chapter 1`, `Ch. 1` → Chapter (English)

## Priority 4: Font Size Mutation

When no structural clues exist:
- Text with font size ≥ 18pt and bold → potential chapter heading
- Text with font size ≥ 14pt and bold → potential section heading
- Compare against median body text size to detect outliers

## Priority 5: Fallback

Content that cannot be assigned to any chapter → mark as `## 未分类内容` (Unclassified Content) and prompt user to specify chapter manually.
