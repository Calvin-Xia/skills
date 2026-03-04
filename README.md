# Skills

A collection of AI agent skills for code analysis and documentation generation.

## Included Skills

### prd-generator

Analyze any code repository to identify innovative feature opportunities and generate comprehensive Product Requirements Documents (PRD).

**Capabilities:**
- Repository structure discovery
- Technology stack analysis
- Feature extraction from source code
- Opportunity identification
- PRD document generation

**Supported Languages:** JavaScript/TypeScript, Python, Go, Rust, Java/Kotlin

### project-architecture-analyzer

Systematically analyze project architecture and generate phased requirement planning with actionable goals.

**Capabilities:**
- Technology stack detection and evaluation
- Module architecture and dependency analysis
- Performance bottleneck and security risk identification
- Phased requirement planning (short/mid/long term)
- Feasibility assessment with measurable acceptance criteria

## Installation

Clone the repository and copy the desired skill to your agent's skills directory:

```bash
git clone https://github.com/your-username/skills.git
cp -r skills/prd-generator $CODEX_HOME/skills/
```

Or install via the skill-installer:

```bash
# List available skills
codex skill list

# Install a specific skill
codex skill install prd-generator
```

## Usage

Each skill is triggered by specific user queries:

**prd-generator:**
- "Analyze this repository and suggest new features"
- "Generate a PRD for this codebase"
- "What features are missing in this project?"

**project-architecture-analyzer:**
- "Analyze my project architecture"
- "Create a development roadmap"
- "What improvements does my project need?"

## Structure

```
skills/
├── prd-generator/
│   ├── SKILL.md           # Skill definition
│   ├── agents/            # Agent configurations
│   └── references/        # Templates and patterns
└── project-architecture-analyzer/
    ├── SKILL.md           # Skill definition
    ├── agents/            # Agent configurations
    ├── assets/            # Report templates
    ├── references/        # Analysis frameworks
    └── scripts/           # Analysis utilities
```

## License

MIT License - see [LICENSE](LICENSE) for details.
