---
name: prd-generator
description: Analyze any code repository to identify innovative feature opportunities and generate comprehensive Product Requirements Documents (PRD). Use when the user wants to (1) analyze a repository's structure and capabilities, (2) identify potential new features or improvements, (3) generate a PRD for new functionality, (4) plan feature development based on existing codebase, or (5) create a skill for future PRD generation. Supports multiple languages (JavaScript/TypeScript, Python, Go, Rust, Java/Kotlin) and frameworks.
---

# PRD Generator

Generate comprehensive Product Requirements Documents by analyzing repository structure, existing features, and identifying innovation opportunities.

## Workflow

### Phase 1: Repository Discovery

Scan the repository to understand its foundation:

1. **Directory Structure**
   - List top-level directories and key subdirectories
   - Identify source code locations (`src/`, `lib/`, `app/`, etc.)
   - Locate configuration and build files

2. **Configuration Files** - Check for these key files:
   - `package.json` (Node.js/JavaScript)
   - `pyproject.toml`, `requirements.txt`, `setup.py` (Python)
   - `Cargo.toml` (Rust)
   - `go.mod` (Go)
   - `pom.xml`, `build.gradle` (Java)
   - `wrangler.toml` (Cloudflare Workers)
   - `vercel.json`, `netlify.toml` (Deployment platforms)

3. **Entry Points**
   - Find main files (`index.js`, `main.py`, `main.go`, `lib.rs`)
   - Identify server files (`server.js`, `app.py`)
   - Locate function handlers (serverless)

### Phase 2: Technology Stack Analysis

Read configuration files to extract:

| File | Extract |
|------|---------|
| `package.json` | dependencies, scripts, framework hints |
| `pyproject.toml` | dependencies, Python version, tools |
| `go.mod` | module name, dependencies |
| `Cargo.toml` | dependencies, Rust edition |
| `wrangler.toml` | Workers config, D1 bindings, KV namespaces |

Identify the architecture pattern:
- **Serverless**: Cloudflare Workers, AWS Lambda, Vercel Functions
- **Monolith**: Single entry point, all-in-one
- **Microservices**: Multiple services, API gateway
- **SPA**: Frontend framework, API calls
- **Full-stack**: Next.js, Nuxt, Remix

### Phase 3: Feature Extraction

Analyze source code to identify existing features:

1. **API Endpoints**
   - Search for route definitions
   - Map HTTP methods and paths
   - Document request/response patterns

2. **UI Components** (if applicable)
   - Locate component files
   - Identify pages/views
   - Map user flows

3. **Data Models**
   - Find schema files (`schema.sql`, `models/`, `prisma/schema.prisma`)
   - Document entities and relationships
   - Note validation rules

4. **Business Logic**
   - Identify service modules
   - Document core workflows
   - Note integration points

### Phase 4: Opportunity Identification

Based on analysis, identify gaps and opportunities:

**Common Missing Features by Project Type:**

| Type | Common Gaps |
|------|-------------|
| Web App | Auth, i18n, a11y, PWA, analytics |
| API | Rate limiting, API docs, versioning, caching |
| Serverless | Error tracking, logging, health checks |
| Mobile | Offline support, push notifications, deep linking |

**Improvement Categories:**
- Security (auth, validation, CORS, secrets)
- Performance (caching, optimization, lazy loading)
- UX (loading states, error handling, accessibility)
- DevOps (CI/CD, monitoring, logging)
- Quality (testing, linting, documentation)

### Phase 5: PRD Generation

Generate a structured PRD using the template in [references/prd-template.md](references/prd-template.md).

**Required Sections:**
1. Executive Summary
2. Problem Statement
3. Proposed Features (with user stories)
4. Technical Specifications
5. Implementation Roadmap
6. Success Metrics
7. Risk Assessment

**User Story Format:**
```
As a [user type], I want to [action] so that [benefit].

Acceptance Criteria:
- Given [context], when [action], then [outcome]
```

## Reference Files

- **[analysis-patterns.md](references/analysis-patterns.md)**: Detailed patterns for analyzing different project types
- **[feature-templates.md](references/feature-templates.md)**: Common feature templates by category
- **[prd-template.md](references/prd-template.md)**: Complete PRD document template

## Output Options

When generating output, offer these options:

1. **Full PRD** - Complete document with all sections
2. **Feature List** - Prioritized list of recommended features
3. **Skill Creation** - Generate a new skill in the repository's `skills/` folder

## Language-Specific Patterns

### JavaScript/TypeScript
- Check `tsconfig.json` for TypeScript configuration
- Look for framework-specific files (`next.config.js`, `nuxt.config.js`)
- Identify testing setup (`jest.config.js`, `vitest.config.ts`)

### Python
- Check for virtual environment indicators
- Look for Django/Flask/FastAPI patterns
- Identify `manage.py` (Django) or `app.py` (Flask)

### Go
- Check `cmd/` directory for entry points
- Look for `internal/` and `pkg/` patterns
- Identify HTTP handlers and middleware

### Rust
- Check `src/main.rs` and `src/lib.rs`
- Look for crate patterns in `Cargo.toml`
- Identify async runtime (tokio, async-std)

## Example Usage

```
User: Analyze this repository and suggest new features

Response:
1. [Discovery] Scan directory structure...
2. [Analysis] Identify tech stack from package.json...
3. [Extraction] Map existing API endpoints...
4. [Synthesis] Identify gaps and opportunities...
5. [Output] Generate PRD with prioritized features...
```
