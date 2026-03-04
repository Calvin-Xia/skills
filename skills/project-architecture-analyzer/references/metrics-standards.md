# Metrics and Standards Reference

## Code Quality Metrics

### Complexity Metrics

| Metric | Description | Threshold |
|--------|-------------|-----------|
| **Cyclomatic Complexity** | Number of independent paths | < 10 per method |
| **Cognitive Complexity** | How hard to understand | < 15 per method |
| **Nesting Depth** | Levels of nested blocks | < 4 levels |
| **Lines of Code (LOC)** | Size indicator | < 500 per file |

### Maintainability Index

```
MI = 171 - 5.2 * ln(V) - 0.23 * G - 16.2 * ln(LOC)

Where:
- V = Halstead Volume
- G = Cyclomatic Complexity
- LOC = Lines of Code

Scale:
- 85-100: Highly Maintainable
- 65-85: Moderately Maintainable
- 0-65: Difficult to Maintain
```

### Code Coverage

| Type | Description | Target |
|------|-------------|--------|
| Line Coverage | % of lines executed | > 80% |
| Branch Coverage | % of branches executed | > 70% |
| Function Coverage | % of functions called | > 90% |

### Technical Debt Ratio

```
TDR = (Remediation Cost / Development Cost) * 100

Where:
- Remediation Cost = Time to fix all issues
- Development Cost = Time to build from scratch

Thresholds:
- < 5%: Excellent
- 5-10%: Good
- > 10%: Needs attention
```

---

## Performance Metrics

### Web Vitals (Core)

| Metric | Description | Good | Needs Work |
|--------|-------------|------|------------|
| **LCP** | Largest Contentful Paint | < 2.5s | > 4.0s |
| **FID** | First Input Delay | < 100ms | > 300ms |
| **CLS** | Cumulative Layout Shift | < 0.1 | > 0.25 |
| **INP** | Interaction to Next Paint | < 200ms | > 500ms |

### Additional Web Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **TTFB** | Time to First Byte | < 800ms |
| **FCP** | First Contentful Paint | < 1.8s |
| **TTI** | Time to Interactive | < 3.8s |
| **SI** | Speed Index | < 3.4s |

### Backend Performance

| Metric | Description | Target |
|--------|-------------|--------|
| **Response Time** | Request to response | < 200ms (p95) |
| **Throughput** | Requests per second | Based on capacity |
| **Error Rate** | Failed requests / total | < 0.1% |
| **Availability** | Uptime percentage | > 99.9% |

### Database Performance

| Metric | Description | Target |
|--------|-------------|--------|
| **Query Time** | Single query execution | < 50ms |
| **Connection Pool** | Active connections | < 80% of limit |
| **Cache Hit Ratio** | Cached queries / total | > 90% |
| **Lock Wait Time** | Time waiting for locks | < 10ms |

---

## Business Metrics

### User Engagement

| Metric | Formula | Use Case |
|--------|---------|----------|
| **DAU** | Daily Active Users | Product health |
| **MAU** | Monthly Active Users | User base size |
| **DAU/MAU Ratio** | DAU / MAU | User stickiness |
| **Session Duration** | Avg time per session | Engagement depth |

### Conversion Metrics

| Metric | Formula | Use Case |
|--------|---------|----------|
| **Conversion Rate** | Conversions / Visitors | Sales funnel |
| **Bounce Rate** | Single page visits / total | Landing page quality |
| **Cart Abandonment** | Abandoned carts / created | Checkout friction |
| **CAC** | Marketing spend / new customers | Acquisition efficiency |

### Retention Metrics

| Metric | Formula | Use Case |
|--------|---------|----------|
| **Retention Rate** | Returning users / total | Product stickiness |
| **Churn Rate** | Lost customers / total | Business health |
| **LTV** | Revenue per customer lifetime | Long-term value |
| **NPS** | Promoters - Detractors | Customer satisfaction |

---

## Acceptance Criteria Templates

### Feature Acceptance

```markdown
## Acceptance Criteria: [Feature Name]

### Functional Requirements
- [ ] User can [action]
- [ ] System responds with [expected behavior]
- [ ] Edge case [X] is handled

### Non-Functional Requirements
- [ ] Response time < [X]ms
- [ ] Works on [browsers/devices]
- [ ] Accessible (WCAG 2.1 AA)

### Integration Requirements
- [ ] API endpoint returns correct response
- [ ] Database updates correctly
- [ ] Third-party service integration works
```

### Bug Fix Acceptance

```markdown
## Acceptance Criteria: [Bug ID]

### Reproduction
- [ ] Bug can be reproduced with steps: [steps]
- [ ] Root cause identified: [cause]

### Fix Verification
- [ ] Bug no longer occurs
- [ ] No regressions in related features
- [ ] Unit test added for fix
```

### Performance Acceptance

```markdown
## Acceptance Criteria: [Performance Goal]

### Baseline
- Current metric: [value]
- Target metric: [value]

### Verification
- [ ] Load test passes with [X] concurrent users
- [ ] Response time < [X]ms at p95
- [ ] Memory usage stable under load
- [ ] No memory leaks detected
```

---

## Quality Gates

### Code Review Checklist

```markdown
## Code Review Quality Gate

### Must Pass
- [ ] All tests pass
- [ ] No security vulnerabilities
- [ ] Code coverage maintained or improved
- [ ] No regressions in existing features

### Should Pass
- [ ] Code follows style guide
- [ ] Documentation updated
- [ ] No code duplication
- [ ] Error handling complete

### Nice to Have
- [ ] Performance optimized
- [ ] Accessibility improved
- [ ] Technical debt reduced
```

### Release Quality Gate

```markdown
## Release Quality Gate

### Pre-Release
- [ ] All P0/P1 bugs resolved
- [ ] Performance benchmarks pass
- [ ] Security scan clean
- [ ] Documentation complete

### Release
- [ ] Changelog updated
- [ ] Version bumped correctly
- [ ] Release notes prepared
- [ ] Rollback plan documented

### Post-Release
- [ ] Monitoring alerts configured
- [ ] Smoke tests pass in production
- [ ] Team notified of release
```

---

## Measurement Tools

### Code Quality

| Tool | Language | Metrics |
|------|----------|---------|
| SonarQube | Multi | All quality metrics |
| ESLint | JavaScript/TypeScript | Code smells, bugs |
| Pylint | Python | Code quality, style |
| RuboCop | Ruby | Style, complexity |
| Golangci-lint | Go | Bugs, style, performance |

### Performance

| Tool | Type | Use Case |
|------|------|----------|
| Lighthouse | Web | Core Web Vitals |
| WebPageTest | Web | Detailed performance |
| JMeter | Load | Backend load testing |
| k6 | Load | API load testing |
| Prometheus | Monitoring | Real-time metrics |

### Coverage

| Tool | Language | Coverage Type |
|------|----------|---------------|
| Istanbul/nyc | JavaScript | Line, branch, function |
| Coverage.py | Python | Line, branch |
| JaCoCo | Java | Line, branch |
| go test -cover | Go | Line, function |
