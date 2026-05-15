# Skills

A collection of AI agent skills for code analysis, documentation generation, and course material processing. All skills are validated against the [writing-skills](https://agentskills.io/specification) quality checklist with **STOP Signs**, **Rationalization Counter-Tables**, and **Red Flags** to ensure reliable agent behavior.

| Skill | Quality Score | Status |
|-------|:------------:|--------|
| course-review-material | 93% (A) | 🟢 Production-ready |
| project-architecture-analyzer | 93% (A) | 🟢 Production-ready |
| prd-generator | 85% (B+) | 🟢 Production-ready |

## Included Skills

### course-review-material

Parse course lecture materials (docx, pptx, pdf, txt) and organize them into structured chapter-by-chapter Markdown review notes for exam preparation.

**Core Principle:** Preserve original text verbatim — no paraphrasing, no rewriting.

**Capabilities:**
- Multi-format extraction: docx, pptx, pdf, txt/md with dedicated Python scripts per format
- Dual-layer PDF processing: text layer (pdfplumber) + image layer (PyMuPDF)
- Embedded image export with multimodal/OCR recognition
- Formula → LaTeX conversion (Chinese math formula support: fractions, limits, integrals, matrices)
- Table → Markdown conversion
- Chapter detection via 5-tier priority heuristics (YAML config, heading styles, numbering patterns, font size mutation, fallback)
- Cross-file deduplication with conflict markers and source annotations
- Interactive YAML-driven chapter configuration

**Supported File Types:** docx, pptx, pdf, txt, md

**Guard Rules:** 6 STOP Signs, 8 Rationalization Counter-Table entries, 6 Red Flags

---

### prd-generator

Analyze code repositories to identify feature gaps, improvement opportunities, and generate comprehensive Product Requirements Documents (PRD).

**Core Principle:** Analyze before you recommend. Every feature proposal must be grounded in the repository's actual structure.

**Capabilities:**
- 5-Phase workflow: Discovery → Tech Stack → Feature Extraction → Opportunity Identification → PRD Generation
- Architecture pattern detection (Serverless, Monolith, Microservices, SPA, Full-stack)
- Existing feature mapping (API endpoints, UI components, data models, business logic)
- Gap analysis by project type (Web App, API, Serverless, Mobile)
- Structured PRD output: Full PRD, Feature List, or Skill Creation
- Multi-format output options with MoSCoW prioritization

**Supported Languages:** JavaScript/TypeScript, Python, Go, Rust, Java/Kotlin

**Guard Rules:** 6 STOP Signs, 6 Rationalization Counter-Table entries, 6 Red Flags

---

### project-architecture-analyzer

Systematically analyze project architecture and generate phased requirement planning with actionable goals.

**Core Principle:** Start with automated analysis (scripts), then validate manually. Classify all issues by P0-P3 severity.

**Capabilities:**
- Automated tech stack detection and evaluation (`analyze_tech_stack.py`)
- Module dependency analysis with circular dependency detection (`detect_dependencies.py`)
- Security risk and performance bottleneck identification
- P0-P3 priority classification with SMART goal planning
- Phased roadmaps: Short-term (1-2mo), Mid-term (3-6mo), Long-term (6+mo)
- Feasibility assessment with resource matching matrix
- Automated report generation (`generate_report.py`)

**Guard Rules:** 6 STOP Signs, 6 Rationalization Counter-Table entries, 6 Red Flags

---

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

**course-review-material:**
- "整理复习资料" / "课程复习" / "期末复习"
- "parse course materials" / "extract lecture content"
- "organize study notes from slides"
- "开卷考试资料整理"

**prd-generator:**
- "Analyze this repository and suggest new features"
- "Generate a PRD for this codebase"
- "What features are missing in this project?"
- "Plan feature development"

**project-architecture-analyzer:**
- "Analyze my project architecture"
- "Create a development roadmap"
- "What improvements does my project need?"
- "Assess technical debt"

## Structure

```
skills/
├── course-review-material/
│   ├── SKILL.md              # Skill definition
│   ├── config_template.yaml  # YAML configuration template
│   ├── assets/               # Output templates
│   │   └── output-templates.md
│   ├── references/           # Detailed processing guides
│   │   ├── file-processing-guide.md
│   │   ├── content-handling.md
│   │   └── chapter-detection.md
│   └── scripts/              # Extraction and integration utilities
│       ├── extract_docx.py
│       ├── extract_pdf.py
│       ├── extract_pptx.py
│       ├── extract_txt.py
│       └── integrate_chapters.py
├── prd-generator/
│   ├── SKILL.md              # Skill definition
│   ├── config_template.yaml  # YAML configuration template
│   ├── agents/               # Agent configurations
│   │   └── openai.yaml
│   └── references/           # Templates and analysis patterns
│       ├── analysis-patterns.md
│       ├── feature-templates.md
│       └── prd-template.md
└── project-architecture-analyzer/
    ├── SKILL.md              # Skill definition
    ├── config_template.yaml  # YAML configuration template
    ├── agents/               # Agent configurations
    │   └── openai.yaml
    ├── assets/               # Report templates
    │   └── report-template/
    │       ├── architecture-report.md
    │       └── roadmap-template.md
    ├── references/           # Analysis frameworks
    │   ├── architecture-patterns.md
    │   ├── tech-stack-templates.md
    │   ├── planning-framework.md
    │   ├── metrics-standards.md
    │   └── risk-assessment.md
    └── scripts/              # Analysis utilities
        ├── analyze_tech_stack.py
        ├── detect_dependencies.py
        └── generate_report.py
```

## Quality Standards

All skills are validated against the [writing-skills](https://agentskills.io/specification) checklist:

| Requirement | course-review | project-arch | prd-gen |
|-------------|:------------:|:------------:|:-------:|
| YAML frontmatter | ✅ | ✅ | ✅ |
| CSO (description) | ✅ | ✅ | ✅ |
| Overview + Core Principle | ✅ | ✅ | ✅ |
| When to Use + Flowchart | ✅ | ✅ | ✅ |
| Environment Check | ✅ | ✅ | ✅ |
| Output Format / Example | ✅ | ✅ | ✅ |
| Quick Reference | ✅ | ✅ | ✅ |
| Common Mistakes | ✅ | ✅ | ✅ |
| STOP Signs (6) | ✅ | ✅ | ✅ |
| Why These Are Hard Stops | ✅ | ✅ | ✅ |
| Rationalization Counter-Table | ✅ | ✅ | ✅ |
| Red Flags | ✅ | ✅ | ✅ |
| Edge Cases | ✅ | ✅ | ✅ |
| Script / Reference Files | ✅ (5+3) | ✅ (3+5) | ✅ (0+3) |

## License

MIT License - see [LICENSE](LICENSE) for details.
