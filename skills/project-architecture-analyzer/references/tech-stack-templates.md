# Tech Stack Templates

## Frontend Tech Stack

### React Ecosystem

```
Core: React 18+
Build: Vite / Next.js / Create React App
State: Redux Toolkit / Zustand / Jotai
Routing: React Router / Next.js Router
Styling: Tailwind CSS / Styled Components / CSS Modules
Testing: Jest + React Testing Library / Vitest
```

**Detection files:**
- `package.json` with `react` dependency
- `jsx/tsx` files
- `react-router`, `redux`, `zustand` imports

---

### Vue Ecosystem

```
Core: Vue 3+
Build: Vite / Vue CLI / Nuxt.js
State: Pinia / Vuex
Routing: Vue Router
Styling: Tailwind CSS / Scoped CSS / CSS Modules
Testing: Vitest + Vue Test Utils
```

**Detection files:**
- `package.json` with `vue` dependency
- `.vue` single file components
- `vue.config.js`, `vite.config.js` with Vue plugin

---

### Angular Ecosystem

```
Core: Angular 16+
Build: Angular CLI
State: NgRx / Akita / Signals
Routing: Angular Router
Styling: SCSS / Tailwind CSS
Testing: Jasmine / Jest + Angular Testing
```

**Detection files:**
- `angular.json`
- `.ts` files with `@Component`, `@NgModule` decorators
- `ng-package.json`

---

### Vanilla / Static

```
Core: HTML + CSS + JavaScript
Build: Vite / Parcel / None
Styling: CSS / SCSS / Tailwind CSS
Testing: Jest / Playwright
```

**Detection files:**
- No framework dependencies
- `.html` files with inline or linked scripts
- Static file structure

---

## Backend Tech Stack

### Node.js Ecosystem

```
Runtime: Node.js 18+
Framework: Express / Fastify / NestJS / Hono
ORM: Prisma / TypeORM / Sequelize
Database: PostgreSQL / MySQL / MongoDB
Auth: Passport.js / JWT / Auth0
```

**Detection files:**
- `package.json` with express, fastify, nest, etc.
- `server.js`, `app.js`, `main.ts`
- `tsconfig.json` for TypeScript

---

### Python Ecosystem

```
Runtime: Python 3.10+
Framework: FastAPI / Django / Flask
ORM: SQLAlchemy / Django ORM
Database: PostgreSQL / MySQL / SQLite
Auth: JWT / OAuth2 / Django Auth
```

**Detection files:**
- `requirements.txt`, `pyproject.toml`, `setup.py`
- `manage.py` (Django)
- `main.py`, `app.py` (FastAPI/Flask)

---

### Java Ecosystem

```
Runtime: JDK 17+
Framework: Spring Boot / Quarkus / Micronaut
ORM: Hibernate / JPA
Database: PostgreSQL / MySQL / Oracle
Build: Maven / Gradle
```

**Detection files:**
- `pom.xml` (Maven)
- `build.gradle` / `build.gradle.kts` (Gradle)
- `Application.java` with `@SpringBootApplication`

---

### Go Ecosystem

```
Runtime: Go 1.21+
Framework: Gin / Echo / Fiber / Chi
ORM: GORM / sqlx
Database: PostgreSQL / MySQL / SQLite
Build: Go modules
```

**Detection files:**
- `go.mod`, `go.sum`
- `main.go`
- `*.go` files

---

## Database Selection Guide

### Relational Databases

| Database | Best For | Scale |
|----------|----------|-------|
| PostgreSQL | Complex queries, JSON support, extensions | Medium-Large |
| MySQL | Web applications, read-heavy workloads | Medium-Large |
| SQLite | Embedded, development, small apps | Small |
| CockroachDB | Distributed SQL, global scale | Large |

---

### NoSQL Databases

| Database | Best For | Scale |
|----------|----------|-------|
| MongoDB | Document storage, flexible schema | Medium-Large |
| Redis | Caching, sessions, real-time | Any |
| DynamoDB | Serverless, auto-scaling | Large |
| Elasticsearch | Search, log analytics | Medium-Large |

---

## DevOps Toolchain

### CI/CD

```
GitHub Actions: .github/workflows/*.yml
GitLab CI: .gitlab-ci.yml
Jenkins: Jenkinsfile
CircleCI: .circleci/config.yml
```

### Containerization

```
Docker: Dockerfile, docker-compose.yml
Kubernetes: k8s/, helm/, *.yaml manifests
```

### Infrastructure

```
Terraform: *.tf files
Pulumi: Pulumi.yaml, *.ts/*.py/*.go
CloudFormation: *.yaml, *.json (AWS)
```

---

## Tech Stack Detection Heuristics

### Priority Order

1. **Config files** - Most reliable indicators
2. **Dependency files** - Package managers
3. **Source code patterns** - Framework-specific imports
4. **Directory structure** - Convention-based detection

### Detection Matrix

| File | Indicates |
|------|-----------|
| `package.json` | Node.js / JavaScript project |
| `requirements.txt` | Python project |
| `go.mod` | Go project |
| `pom.xml` | Java (Maven) project |
| `Cargo.toml` | Rust project |
| `composer.json` | PHP project |
| `Gemfile` | Ruby project |

### Framework Detection

| Import/Pattern | Framework |
|----------------|-----------|
| `import React` | React |
| `import { createApp }` | Vue |
| `@Component` | Angular |
| `from fastapi import` | FastAPI |
| `from django` | Django |
| `@SpringBootApplication` | Spring Boot |
| `from flask import` | Flask |
| `gin.Default()` | Gin (Go) |
