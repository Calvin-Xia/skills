---
name: skills-index
description: Index of available AI agent skills for code analysis and documentation generation.
---

# Skills Index

This directory contains AI agent skills that extend agent capabilities for specific tasks.

## Available Skills

| Skill | Description | Trigger Keywords |
|-------|-------------|------------------|
| [prd-generator](./prd-generator/SKILL.md) | Generate PRD documents from repository analysis | "analyze repository", "generate PRD", "suggest features" |
| [project-architecture-analyzer](./project-architecture-analyzer/SKILL.md) | Analyze architecture and create development roadmaps | "analyze architecture", "development roadmap", "improvements" |

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
