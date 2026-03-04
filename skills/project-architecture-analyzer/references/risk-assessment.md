# Risk Assessment Framework

## Risk Categories

### Technical Risks

| Risk Type | Examples | Impact |
|-----------|----------|--------|
| **Architecture** | Scalability limits, coupling issues | High |
| **Security** | Vulnerabilities, data breaches | Critical |
| **Performance** | Bottlenecks, resource exhaustion | High |
| **Dependency** | Outdated packages, license issues | Medium |
| **Technical Debt** | Code quality, maintainability | Medium |

### Business Risks

| Risk Type | Examples | Impact |
|-----------|----------|--------|
| **Market** | Competition, demand changes | High |
| **Compliance** | Regulatory requirements | Critical |
| **Resource** | Team availability, skills gap | Medium |
| **Timeline** | Missed deadlines, scope creep | Medium |
| **Budget** | Cost overruns, funding issues | High |

---

## Risk Matrix

### Probability vs Impact

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

### Risk Scoring

| Score | Level | Action Required |
|-------|-------|-----------------|
| 1-3 | Low | Monitor, document |
| 4-6 | Medium | Plan mitigation |
| 7-9 | High | Immediate action |
| 10 | Critical | Escalate, block |

---

## Risk Assessment Process

### Step 1: Risk Identification

```markdown
## Risk Identification Checklist

### Technical
- [ ] Single points of failure
- [ ] Unmaintained dependencies
- [ ] Known security vulnerabilities
- [ ] Performance bottlenecks
- [ ] Scalability limitations
- [ ] Data loss scenarios
- [ ] Integration failures

### Operational
- [ ] Deployment failures
- [ ] Monitoring gaps
- [ ] Backup/recovery issues
- [ ] Access control weaknesses
- [ ] Documentation gaps

### External
- [ ] Third-party service outages
- [ ] API changes/deprecation
- [ ] Regulatory changes
- [ ] Vendor lock-in
```

### Step 2: Risk Analysis

```markdown
## Risk Analysis Template

### Risk: [Risk Name]

**Category:** [Technical/Business/Operational]
**Probability:** [Low/Medium/High]
**Impact:** [Low/Medium/High/Critical]
**Risk Score:** [1-10]

**Description:**
[Detailed description of the risk]

**Root Cause:**
[What causes this risk to exist]

**Affected Components:**
- Component 1
- Component 2

**Current Controls:**
[Existing mitigations]

**Residual Risk:**
[Remaining risk after controls]
```

### Step 3: Risk Response Planning

```markdown
## Risk Response Options

### Avoid
- Eliminate the risk entirely
- Example: Remove risky feature

### Transfer
- Shift risk to another party
- Example: Insurance, outsourcing

### Mitigate
- Reduce probability or impact
- Example: Add redundancy, monitoring

### Accept
- Acknowledge and monitor
- Example: Low-impact risks
```

---

## Mitigation Strategies

### Architecture Risks

| Risk | Mitigation |
|------|------------|
| Single point of failure | Add redundancy, load balancing |
| Tight coupling | Refactor to loose coupling, interfaces |
| Scalability limits | Horizontal scaling, caching |
| Data loss | Backups, replication, disaster recovery |

### Security Risks

| Risk | Mitigation |
|------|------------|
| SQL Injection | Parameterized queries, ORM |
| XSS | Input sanitization, CSP headers |
| Auth bypass | Multi-factor auth, session management |
| Data exposure | Encryption, access controls |

### Performance Risks

| Risk | Mitigation |
|------|------------|
| Slow queries | Indexing, query optimization |
| Memory leaks | Profiling, proper cleanup |
| N+1 queries | Eager loading, batching |
| Large payloads | Pagination, compression |

### Dependency Risks

| Risk | Mitigation |
|------|------------|
| Outdated packages | Automated updates (Dependabot) |
| Security vulnerabilities | Regular scanning (Snyk, npm audit) |
| License issues | License compliance tools |
| Abandoned packages | Evaluate alternatives, fork if needed |

---

## Risk Register Template

```markdown
# Project Risk Register

| ID | Risk | Category | Probability | Impact | Score | Owner | Status | Mitigation |
|----|------|----------|-------------|--------|-------|-------|--------|------------|
| R1 | [Risk name] | [Cat] | [P] | [I] | [S] | [Name] | [Status] | [Strategy] |
| R2 | ... | ... | ... | ... | ... | ... | ... | ... |

## Summary
- Total Risks: X
- Critical: X
- High: X
- Medium: X
- Low: X
```

---

## Risk Monitoring

### Key Risk Indicators (KRIs)

| KRI | Threshold | Action |
|-----|-----------|--------|
| Error rate | > 1% | Investigate immediately |
| Response time | > 500ms | Performance review |
| Security alerts | Any critical | Patch within 24h |
| Test coverage | < 70% | Add tests before new features |
| Technical debt ratio | > 10% | Schedule refactoring |

### Risk Review Cadence

| Frequency | Activity |
|-----------|----------|
| Daily | Monitor KRIs, check alerts |
| Weekly | Review new risks, update status |
| Monthly | Full risk register review |
| Quarterly | Strategic risk assessment |

---

## Risk Communication

### Risk Report Template

```markdown
# Risk Report - [Date]

## Executive Summary
- Total active risks: X
- New risks this period: X
- Mitigated risks: X
- Escalated risks: X

## Critical Risks
[List of critical risks requiring immediate attention]

## Trend Analysis
[Changes in risk profile over time]

## Recommendations
[Priority actions for stakeholders]
```

### Stakeholder Communication

| Audience | Content | Frequency |
|----------|---------|-----------|
| Executive | Summary, critical risks | Monthly |
| Team | All risks, mitigation status | Weekly |
| Technical | Detailed technical risks | As needed |
| External | Relevant risks only | As required |

---

## Risk Assessment Tools

### Automated Scanning

| Tool | Purpose |
|------|---------|
| Snyk | Dependency vulnerabilities |
| SonarQube | Code quality, security |
| OWASP ZAP | Web app security |
| Trivy | Container vulnerabilities |
| Checkov | Infrastructure as code |

### Manual Assessment

| Technique | Use Case |
|-----------|----------|
| Threat modeling | Security architecture |
| Code review | Quality, security |
| Architecture review | Design risks |
| Load testing | Performance risks |
| Penetration testing | Security validation |
