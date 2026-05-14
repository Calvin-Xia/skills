# Output Templates

## Chapter Output Format

Each chapter file (`ch01-xxx.md`) should follow this structure:

```markdown
# 第1章 {章节标题}

> **来源**: {讲义名称}, {PPT名称}
> **关键词**: {keyword1}, {keyword2}, ...

## 1.1 {节标题}

{正文内容 - 保留原文表述}

![图片描述](images/img_001.png)

<!-- image source: img_001.png -->

这是多模态识别后内联的文字内容...

### 关键公式

$$E = mc^2$$

### 代码示例

```python
def example():
    pass
```

## 1.2 {节标题}

...
```

## Index File Format

```markdown
# {课程名称} - 复习资料目录

> **学期**: {学期}
> **教师**: {教师名}
> **生成时间**: {生成时间}
> **源文件**: {文件列表}

## 目录

| 章节 | 文件 |
|------|------|
| 第1章 函数与极限 | [ch01-函数与极限.md](ch01-函数与极限.md) |
| 第2章 导数与微分 | [ch02-导数与微分.md](ch02-导数与微分.md) |
| ... | ... |

## 未分类内容

[待分类内容.md](待分类内容.md) *(如有)*

## 附录

### 原始文件提取结果

| 源文件 | 提取结果 |
|--------|----------|
| 高数讲义.docx | [高数讲义/extracted.md](../高数讲义/extracted.md) |
| 上课PPT.pptx | [上课PPT/extracted.md](../上课PPT/extracted.md) |
```
