# Architecture Patterns Reference

## Common Architecture Patterns

### 1. Monolithic Architecture

**Characteristics:**
- Single deployable unit
- Shared database
- Tightly coupled components
- Simple deployment

**Indicators in codebase:**
- Single main entry point
- Shared models/DTOs across all features
- Direct function calls between modules
- Single build output

**When suitable:**
- Small teams (< 10 developers)
- Early-stage startups
- Simple domain logic
- Quick time-to-market needed

---

### 2. MVC (Model-View-Controller)

**Characteristics:**
- Separation of concerns
- Models handle data
- Views handle presentation
- Controllers handle logic

**Indicators in codebase:**
- `/models`, `/views`, `/controllers` directories
- Clear separation between data and UI
- Template files for views
- Route handlers as controllers

**When suitable:**
- Web applications with traditional server rendering
- Content management systems
- E-commerce platforms

---

### 3. MVVM (Model-View-ViewModel)

**Characteristics:**
- Two-way data binding
- ViewModels as intermediaries
- Reactive updates
- Testable business logic

**Indicators in codebase:**
- Vue.js, Angular, or WPF usage
- Observable/state management patterns
- Template bindings
- Computed properties

**When suitable:**
- Rich client applications
- Single-page applications (SPAs)
- Mobile applications

---

### 4. Microservices Architecture

**Characteristics:**
- Independent deployable services
- Service-specific databases
- API-based communication
- Decentralized governance

**Indicators in codebase:**
- Multiple repositories or service folders
- Docker/Kubernetes configs
- API gateway patterns
- Event-driven communication (Kafka, RabbitMQ)

**When suitable:**
- Large teams (> 50 developers)
- High scalability requirements
- Complex domain with bounded contexts
- Need for technology diversity

---

### 5. Serverless Architecture

**Characteristics:**
- Function-as-a-Service (FaaS)
- Event-driven execution
- No server management
- Pay-per-use pricing

**Indicators in codebase:**
- AWS Lambda, Azure Functions, GCP Functions
- Serverless Framework or SAM templates
- API Gateway configurations
- Event triggers (S3, SQS, SNS)

**When suitable:**
- Unpredictable traffic patterns
- Event-driven workloads
- Cost optimization needs
- Quick prototyping

---

### 6. Layered Architecture (N-Tier)

**Characteristics:**
- Horizontal layers
- Presentation layer
- Business logic layer
- Data access layer

**Indicators in codebase:**
- `/api`, `/service`, `/repository`, `/dao` directories
- Dependency injection patterns
- Interface-based design
- Clear layer boundaries

**When suitable:**
- Enterprise applications
- Traditional business systems
- Teams with clear role separation

---

## Architecture Anti-Patterns

### 1. Big Ball of Mud

**Signs:**
- No clear structure
- Circular dependencies
- God classes (> 500 lines)
- Everything depends on everything

**Remediation:**
- Identify bounded contexts
- Extract modules incrementally
- Establish clear interfaces

---

### 2. Spaghetti Code

**Signs:**
- No separation of concerns
- Mixed business and UI logic
- Global state abuse
- Copy-paste programming

**Remediation:**
- Apply MVC/MVVM patterns
- Introduce service layer
- Refactor to pure functions

---

### 3. Golden Hammer

**Signs:**
- Using same technology for all problems
- Forcing patterns where they don't fit
- Ignoring domain-specific needs

**Remediation:**
- Evaluate each problem independently
- Consider multiple solutions
- Prototype alternatives

---

### 4. Copy-Paste Programming

**Signs:**
- Duplicated code blocks
- Similar files with minor variations
- No shared utilities

**Remediation:**
- Extract common functions
- Create utility modules
- Apply DRY principle

---

## Architecture Evolution Strategies

### From Monolith to Microservices

```
Phase 1: Modularize
├── Identify bounded contexts
├── Create module boundaries
└── Establish interfaces

Phase 2: Extract Services
├── Start with least coupled modules
├── Create API contracts
└── Deploy independently

Phase 3: Database Split
├── Identify data ownership
├── Create service-specific schemas
└── Implement data synchronization
```

### From MVC to MVVM

```
Phase 1: Add State Management
├── Introduce observable patterns
├── Create view models
└── Bind views to view models

Phase 2: Remove Server Dependencies
├── Move logic to client
├── Create API endpoints
└── Implement client-side routing
```

---

## Architecture Decision Record (ADR) Template

```markdown
# ADR-XXX: [Decision Title]

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
[What is the issue being addressed?]

## Decision
[What is the change being proposed/made?]

## Consequences
[What are the positive and negative outcomes?]

## Alternatives Considered
[What other options were evaluated?]
```
