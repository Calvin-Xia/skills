# Planning Framework Guide

## SMART Goals Framework

### Definition

- **S**pecific: Clear, well-defined objective
- **M**easurable: Quantifiable success criteria
- **A**chievable: Realistic given constraints
- **R**elevant: Aligned with broader goals
- **T**ime-bound: Clear deadline

### Example

```markdown
# Bad Goal
"Improve performance"

# SMART Goal
"Reduce page load time from 3.5s to under 2s for 95% of users 
by implementing lazy loading and image optimization within 6 weeks"
```

---

## OKR Framework (Objectives and Key Results)

### Structure

```
Objective: [Qualitative goal to achieve]
├── Key Result 1: [Measurable outcome]
├── Key Result 2: [Measurable outcome]
└── Key Result 3: [Measurable outcome]
```

### Example

```
Objective: Improve user experience on mobile devices

Key Results:
├── KR1: Reduce mobile bounce rate from 65% to 45%
├── KR2: Increase mobile session duration by 30%
└── KR3: Achieve 4.5+ app store rating (from 3.8)
```

---

## MoSCoW Prioritization

### Categories

| Priority | Definition | Action |
|----------|------------|--------|
| **M**ust Have | Critical for success | Deliver first |
| **S**hould Have | Important but not critical | Deliver if possible |
| **C**ould Have | Nice to have | Backlog |
| **W**on't Have | Not in scope | Explicitly excluded |

### Decision Matrix

```
High Business Value + Low Effort = Must Have
High Business Value + High Effort = Should Have
Low Business Value + Low Effort = Could Have
Low Business Value + High Effort = Won't Have
```

---

## Agile Planning

### Sprint Planning

```
Sprint Duration: 2 weeks
├── Sprint Goal: [Single sentence objective]
├── Sprint Backlog: [Selected user stories]
├── Capacity: [Team availability in hours]
└── Velocity: [Historical story points per sprint]
```

### User Story Format

```
As a [type of user],
I want [some goal],
So that [some reason].

Acceptance Criteria:
├── Given [context]
├── When [action]
└── Then [outcome]
```

---

## Roadmap Planning

### Short-term (1-2 months)

**Focus:** Quick wins, critical fixes, immediate value

**Template:**
```markdown
## Short-term Goals (1-2 months)

### Goal 1: [Title]
- **Description:** [What and why]
- **Success Metrics:** [Quantifiable measures]
- **Acceptance Criteria:**
  - [ ] Criterion 1
  - [ ] Criterion 2
- **Resources Required:** [Team, tools, budget]
- **Dependencies:** [What must happen first]
- **Risks:** [Potential blockers]
```

---

### Mid-term (3-6 months)

**Focus:** Architecture improvements, feature development, technical debt

**Template:**
```markdown
## Mid-term Goals (3-6 months)

### Goal 1: [Title]
- **Description:** [What and why]
- **Milestones:**
  - M1: [Month 1 deliverable]
  - M2: [Month 2 deliverable]
  - M3: [Month 3 deliverable]
- **Success Metrics:** [Quantifiable measures]
- **Dependencies:** [Cross-team, external]
- **Resource Requirements:** [Detailed breakdown]
```

---

### Long-term (6+ months)

**Focus:** Strategic initiatives, platform evolution, team growth

**Template:**
```markdown
## Long-term Goals (6+ months)

### Goal 1: [Title]
- **Vision:** [Future state description]
- **Strategic Value:** [Business impact]
- **Evolution Path:**
  - Phase 1: [Foundation]
  - Phase 2: [Expansion]
  - Phase 3: [Optimization]
- **Success Metrics:** [Long-term KPIs]
- **Investment Required:** [Time, people, money]
```

---

## Effort Estimation

### Story Points Scale (Fibonacci)

| Points | Complexity | Risk | Effort |
|--------|------------|------|--------|
| 1 | Trivial | None | Hours |
| 2 | Simple | Low | Half day |
| 3 | Moderate | Some | 1-2 days |
| 5 | Complex | Medium | 3-5 days |
| 8 | Very Complex | High | 1-2 weeks |
| 13 | Epic | Very High | Sprint+ |

### T-Shirt Sizing

| Size | Story Points | Duration |
|------|--------------|----------|
| XS | 1-2 | Hours |
| S | 3 | 1-2 days |
| M | 5 | 3-5 days |
| L | 8 | 1-2 weeks |
| XL | 13+ | Sprint+ |

---

## Planning Anti-Patterns

### 1. Planning Fallacy

**Sign:** Consistently underestimating effort

**Fix:**
- Use historical data
- Add buffer (20-30%)
- Break down large items

### 2. Scope Creep

**Sign:** Continuous addition of requirements

**Fix:**
- Lock scope per sprint
- Use change request process
- Maintain backlog for new items

### 3. Analysis Paralysis

**Sign:** Over-planning, delayed execution

**Fix:**
- Time-box planning sessions
- Start with MVP approach
- Iterate and refine

---

## Progress Tracking

### Burndown Chart

```
Story Points
    │
100 │╲
    │ ╲
 75 │  ╲
    │   ╲
 50 │    ╲
    │     ╲
 25 │      ╲
    │       ╲
  0 │────────╲────────
    D1  D5  D10  D15
        Days
```

### Key Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Velocity | Story points completed / sprint | Stable or increasing |
| Cycle Time | Time from start to done | Decreasing |
| Throughput | Items completed / week | Stable |
| Lead Time | Time from request to delivery | Decreasing |
