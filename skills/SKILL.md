---
name: skills-index
description: Index of available AI agent skills for code analysis and documentation generation.
---

# Skills Index

This directory contains AI agent skills that extend agent capabilities for specific tasks.

## Available Skills

| Skill | Description | Trigger Keywords |
|-------|-------------|------------------|
| [course-review-material](./course-review-material/SKILL.md) | Parse course materials into chapter-organized Markdown review notes | "整理复习资料", "期末复习", "parse course materials", "organize study notes" |
| [prd-generator](./prd-generator/SKILL.md) | Analyze repositories for feature opportunities and generate PRDs | "analyze repository", "generate PRD", "what features are missing", "plan feature development" |
| [project-architecture-analyzer](./project-architecture-analyzer/SKILL.md) | Architecture analysis and phased development roadmaps | "analyze architecture", "development roadmap", "technical debt", "plan next steps" |

## Skill Structure

Each skill follows a standard structure:

```
skill-name/
├── SKILL.md           # Skill definition and workflow
├── agents/            # Agent-specific configurations
├── references/        # Templates, patterns, and frameworks
├── assets/            # Static resources (optional)
└── scripts/           # Utility scripts (optional)
```

## Adding a New Skill

1. Create a new directory under `skills/`
2. Add a `SKILL.md` file with frontmatter containing `name` and `description`
3. Include necessary references, assets, or scripts
4. Update this index file

## Skill Metadata

Each `SKILL.md` must include YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description of what the skill does.
---
```
