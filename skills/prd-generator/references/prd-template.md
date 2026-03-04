# PRD Template

## Document Structure

```markdown
# [Feature Name] - Product Requirements Document

## Executive Summary
[2-3 sentences summarizing the feature and its value]

## Problem Statement

### Current State
[Describe the current situation]

### Pain Points
- [Pain point 1]
- [Pain point 2]
- [Pain point 3]

### Opportunity
[Describe the opportunity this feature addresses]

## Proposed Solution

### Overview
[High-level description of the solution]

### User Stories

#### Story 1: [Story Title]
**As a** [user type]
**I want to** [action]
**So that** [benefit]

**Acceptance Criteria:**
- Given [context], when [action], then [outcome]
- Given [context], when [action], then [outcome]

#### Story 2: [Story Title]
[Repeat format]

### Non-Functional Requirements
- **Performance**: [Response time, throughput requirements]
- **Security**: [Security requirements]
- **Scalability**: [Scale requirements]
- **Accessibility**: [A11y requirements]

## Technical Specifications

### Architecture
[Describe the technical approach]

### API Changes
[Document new or modified endpoints]

### Database Changes
[Document schema changes]

### Dependencies
[List new dependencies required]

### Security Considerations
[Document security implications]

## Implementation Roadmap

### Phase 1: MVP
- [ ] [Task 1]
- [ ] [Task 2]
- [ ] [Task 3]

### Phase 2: Enhancement
- [ ] [Task 1]
- [ ] [Task 2]

### Phase 3: Polish
- [ ] [Task 1]
- [ ] [Task 2]

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| [Metric 1] | [Target] | [How to measure] |
| [Metric 2] | [Target] | [How to measure] |

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | High/Medium/Low | High/Medium/Low | [Mitigation strategy] |
| [Risk 2] | High/Medium/Low | High/Medium/Low | [Mitigation strategy] |

## Open Questions
- [Question 1]
- [Question 2]

## Appendix

### Related Documents
- [Link to related specs]
- [Link to design docs]

### Glossary
| Term | Definition |
|------|------------|
| [Term 1] | [Definition] |
```

## User Story Template

```markdown
### [Story ID]: [Story Title]

**As a** [specific user type]
**I want to** [specific action]
**So that** [specific benefit/value]

**Priority:** MoSCoW (Must/Should/Could/Won't)
**Story Points:** [Estimate]

**Acceptance Criteria:**
1. **Given** [initial context/precondition]
   **When** [action is taken]
   **Then** [expected outcome]

2. **Given** [alternative context]
   **When** [action is taken]
   **Then** [expected outcome]

**Technical Notes:**
- [Implementation consideration 1]
- [Implementation consideration 2]

**Dependencies:**
- [Dependency 1]
- [Dependency 2]
```

## Technical Spec Template

```markdown
## Technical Specification: [Feature Name]

### Overview
[Brief technical summary]

### Architecture Diagram
```
[ASCII diagram or description of architecture]
┌─────────┐     ┌─────────┐     ┌─────────┐
│ Client  │────▶│ Server  │────▶│ Database│
└─────────┘     └─────────┘     └─────────┘
```

### API Specification

#### Endpoint: [HTTP Method] [Path]
**Description:** [What this endpoint does]

**Request:**
```json
{
  "field1": "type",
  "field2": "type"
}
```

**Response:**
```json
{
  "field1": "type",
  "field2": "type"
}
```

**Error Responses:**
- `400 Bad Request` - [When this occurs]
- `401 Unauthorized` - [When this occurs]
- `500 Internal Server Error` - [When this occurs]

### Database Schema

```sql
CREATE TABLE example (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Security Considerations
- [Security consideration 1]
- [Security consideration 2]

### Performance Considerations
- [Performance consideration 1]
- [Performance consideration 2]
```

## Risk Assessment Template

```markdown
## Risk Assessment

### Technical Risks

| Risk | Probability | Impact | Score | Mitigation | Owner |
|------|-------------|--------|-------|------------|-------|
| [Risk] | H/M/L | H/M/L | P×I | [Strategy] | [Name] |

### Business Risks

| Risk | Probability | Impact | Score | Mitigation | Owner |
|------|-------------|--------|-------|------------|-------|
| [Risk] | H/M/L | H/M/L | P×I | [Strategy] | [Name] |

### Risk Score Matrix
```
              Impact
         Low    Med    High
    ┌────────┬────────┬────────┐
  H │   3    │   6    │   9    │
P   ├────────┼────────┼────────┤
r   M │   2    │   4    │   6    │
o   ├────────┼────────┼────────┤
b   L │   1    │   2    │   3    │
    └────────┴────────┴────────┘
```
```

## Implementation Roadmap Template

```markdown
## Implementation Roadmap

### Sprint 1: Foundation
**Duration:** 2 weeks
**Goal:** [Sprint goal]

**Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

**Dependencies:**
- [Dependency 1]

### Sprint 2: Core Features
**Duration:** 2 weeks
**Goal:** [Sprint goal]

**Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

**Dependencies:**
- Sprint 1 completion

### Sprint 3: Polish & Launch
**Duration:** 1 week
**Goal:** [Sprint goal]

**Deliverables:**
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

**Dependencies:**
- Sprint 2 completion

### Milestones
| Milestone | Date | Criteria |
|-----------|------|----------|
| MVP Ready | [Date] | [Criteria] |
| Beta Launch | [Date] | [Criteria] |
| Full Launch | [Date] | [Criteria] |
```

## Success Metrics Template

```markdown
## Success Metrics

### Key Performance Indicators (KPIs)

| KPI | Current | Target | Timeline |
|-----|---------|--------|----------|
| [KPI 1] | [Value] | [Value] | [Date] |
| [KPI 2] | [Value] | [Value] | [Date] |

### User Metrics
- **Adoption Rate:** [Target]% of users within [timeframe]
- **Engagement:** [Target] sessions per user per [period]
- **Retention:** [Target]% retention after [period]

### Technical Metrics
- **Performance:** [Target]ms response time
- **Uptime:** [Target]% availability
- **Error Rate:** <[Target]%

### Business Metrics
- **Conversion:** [Target]% conversion rate
- **Revenue Impact:** [Target] $ or % increase
- **Cost Savings:** [Target] $ or % reduction
```
