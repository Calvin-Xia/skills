---
name: project-architecture-analyzer
description: Systematically analyze project architecture and generate phased requirement planning. Use when users request architecture analysis, project planning, technical debt assessment, improvement suggestions, or phased goal setting. Triggers on queries like "analyze my project architecture", "create a development roadmap", "what improvements does my project need", or "plan next steps for my codebase".
---

# Project Architecture Analyzer

Systematically analyze project architecture and generate phased requirement planning with actionable goals.

## Overview

This skill provides comprehensive project analysis including:
- Technology stack detection and evaluation
- Module architecture and dependency analysis
- Performance bottleneck and security risk identification
- Phased requirement planning (short/mid/long term)
- Feasibility assessment with measurable acceptance criteria

## Workflow

### Phase 1: Architecture Analysis

#### 1.1 Project Scanning

Run the tech stack analyzer to detect project technologies:

```bash
python scripts/analyze_tech_stack.py <project_path>
```

This outputs:
- Project type classification
- Language distribution
- Framework detection (frontend/backend)
- Database identification
- DevOps tooling

#### 1.2 Dependency Analysis

Run the dependency detector to analyze module relationships:

```bash
python scripts/detect_dependencies.py <project_path>
```

This outputs:
- Module count and types
- Dependency graph
- Circular dependency detection
- Coupling metrics

#### 1.3 Manual Review

Complement automated analysis with:

- Directory structure review using `LS` tool
- Key configuration file inspection
- Entry point identification
- Critical path analysis

**Key files to check:**
- `package.json`, `requirements.txt`, `go.mod`, `pom.xml`
- Configuration files (`.env.example`, `config.*`)
- Entry points (`main.*`, `app.*`, `index.*`)

### Phase 2: Issue Identification

#### Priority Classification

| Priority | Name | Criteria |
|----------|------|----------|
| **P0** | Critical | Security vulnerabilities, data loss risk, blocking bugs |
| **P1** | High | Circular dependencies, architecture violations, performance issues |
| **P2** | Medium | Code smells, maintainability concerns, missing tests |
| **P3** | Low | Style issues, documentation gaps, minor optimizations |

#### Analysis Areas

1. **Architecture Issues**
   - Circular dependencies
   - Tight coupling (instability > 0.7)
   - Missing layer separation
   - God modules (> 500 LOC)

2. **Security Risks**
   - See `references/risk-assessment.md` for checklist
   - Check for exposed secrets
   - Validate authentication/authorization
   - Review dependency vulnerabilities

3. **Performance Bottlenecks**
   - N+1 query patterns
   - Missing caching
   - Large bundle sizes
   - Unoptimized assets

4. **Technical Debt**
   - Outdated dependencies
   - Missing tests
   - Code duplication
   - Missing documentation

### Phase 3: Requirement Planning

#### Short-term Goals (1-2 months)

Focus on quick wins and critical fixes:

```markdown
## Short-term Goals

### Goal: [Title]
- **Priority**: P0/P1
- **Description**: [What and why]
- **Success Metrics**: [Quantifiable measures]
- **Acceptance Criteria**:
  - [ ] Criterion 1
  - [ ] Criterion 2
- **Effort**: [Story points or time estimate]
- **Dependencies**: [What must happen first]
```

**Typical short-term items:**
- Fix critical security issues
- Resolve circular dependencies
- Add missing tests for critical paths
- Update vulnerable dependencies

#### Mid-term Goals (3-6 months)

Focus on architecture improvements:

```markdown
## Mid-term Goals

### Goal: [Title]
- **Description**: [What and why]
- **Milestones**:
  - M1 (Month 1): [Deliverable]
  - M2 (Month 2): [Deliverable]
  - M3 (Month 3): [Deliverable]
- **Success Metrics**: [Quantifiable measures]
- **Resource Requirements**: [Team, tools, budget]
```

**Typical mid-term items:**
- Refactor to reduce coupling
- Implement CI/CD pipeline
- Add comprehensive test coverage
- Performance optimization

#### Long-term Goals (6+ months)

Focus on strategic initiatives:

```markdown
## Long-term Goals

### Goal: [Title]
- **Vision**: [Future state description]
- **Strategic Value**: [Business impact]
- **Evolution Path**:
  - Phase 1: [Foundation]
  - Phase 2: [Expansion]
  - Phase 3: [Optimization]
- **Investment Required**: [Time, people, budget]
```

**Typical long-term items:**
- Architecture migration (monolith to microservices)
- Platform modernization
- Team capability building
- Technical debt elimination

### Phase 4: Feasibility Assessment

#### Technical Feasibility

Evaluate each goal against:
- Current team skills
- Technology compatibility
- Integration complexity
- Migration risks

#### Resource Assessment

| Resource | Available | Required | Gap |
|----------|-----------|----------|-----|
| Developers | X | Y | Z |
| Time | X weeks | Y weeks | Z |
| Budget | $X | $Y | $Z |

#### Risk Matrix

See `references/risk-assessment.md` for detailed framework.

```
              IMPACT
         Low    Med    High
    ┌────────┬────────┬────────┐
High│ Medium │ High   │ Critical│
    ├────────┼────────┼────────┤
Med │ Low    │ Medium │ High   │
    ├────────┼────────┼────────┤
Low │ Low    │ Low    │ Medium │
    └────────┴────────┴────────┘
         PROBABILITY
```

### Phase 5: Report Generation

Generate the final report:

```bash
python scripts/generate_report.py tech_stack.json dependencies.json [project_name]
```

Or use the template in `assets/report-template/architecture-report.md`.

## Output Format

### Architecture Analysis Report

```markdown
# Project Architecture Analysis Report

## Executive Summary
- Project Type: [Classification]
- Tech Stack: [Key technologies]
- Health Score: [Excellent/Good/Fair/Needs Improvement]

## Technology Stack Analysis
### Languages
### Frameworks
### Databases
### DevOps

## Module Architecture
### Entry Points
### Core Modules
### Utility Modules
### Dependency Graph

## Issues and Risks
### P0 - Critical
### P1 - High
### P2 - Medium
### P3 - Low

## Recommendations
```

### Requirement Planning Document

```markdown
# Phased Requirement Planning

## Project Background
[Key findings from architecture analysis]

## Short-term Goals (1-2 months)
[Quick wins and critical fixes]

## Mid-term Goals (3-6 months)
[Architecture improvements]

## Long-term Goals (6+ months)
[Strategic initiatives]

## Feasibility Assessment
### Technical Feasibility
### Resource Matching
### Risk Matrix

## Appendix
### Glossary
### Reference Documents
```

## Reference Files

| File | Purpose |
|------|---------|
| `references/architecture-patterns.md` | Common patterns and anti-patterns |
| `references/tech-stack-templates.md` | Tech stack detection heuristics |
| `references/planning-framework.md` | SMART goals, OKR, MoSCoW methods |
| `references/metrics-standards.md` | Quality metrics and acceptance criteria |
| `references/risk-assessment.md` | Risk identification and mitigation |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/analyze_tech_stack.py` | Detect project technologies |
| `scripts/detect_dependencies.py` | Analyze module dependencies |
| `scripts/generate_report.py` | Generate structured reports |

## Best Practices

1. **Start with automated analysis** - Run scripts first, then validate manually
2. **Prioritize by impact** - Focus on P0/P1 issues before optimization
3. **Make goals measurable** - Use SMART criteria for all recommendations
4. **Consider constraints** - Account for team size, timeline, and budget
5. **Iterate incrementally** - Break large changes into smaller, safe steps
