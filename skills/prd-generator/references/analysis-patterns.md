# Repository Analysis Patterns

## Directory Structure Patterns

### JavaScript/TypeScript Projects

```
project/
├── src/              # Source code
│   ├── components/   # UI components
│   ├── pages/        # Page components (Next.js, etc.)
│   ├── api/          # API routes
│   ├── lib/          # Utilities
│   └── hooks/        # React hooks
├── public/           # Static assets
├── tests/            # Test files
├── package.json      # Dependencies
└── tsconfig.json     # TypeScript config
```

### Python Projects

```
project/
├── src/
│   └── package/      # Main package
│       ├── __init__.py
│       ├── models/   # Data models
│       ├── views/    # Views/controllers
│       └── utils/    # Utilities
├── tests/            # Test files
├── pyproject.toml    # Project config
└── requirements.txt  # Dependencies
```

### Go Projects

```
project/
├── cmd/              # Entry points
│   └── server/
│       └── main.go
├── internal/         # Private code
│   ├── handlers/
│   └── models/
├── pkg/              # Public code
├── go.mod            # Module definition
└── go.sum            # Dependencies lock
```

### Rust Projects

```
project/
├── src/
│   ├── main.rs       # Binary entry
│   ├── lib.rs        # Library root
│   └── bin/          # Additional binaries
├── Cargo.toml        # Package manifest
└── Cargo.lock        # Dependencies lock
```

## Configuration File Detection

### Package Managers

| File | Language | Key Information |
|------|----------|-----------------|
| `package.json` | JavaScript | dependencies, scripts, engines |
| `yarn.lock` | JavaScript | locked dependencies |
| `pnpm-lock.yaml` | JavaScript | locked dependencies |
| `pyproject.toml` | Python | dependencies, build config |
| `requirements.txt` | Python | dependencies |
| `Pipfile` | Python | pipenv dependencies |
| `go.mod` | Go | module, dependencies |
| `Cargo.toml` | Rust | dependencies, features |
| `pom.xml` | Java | Maven dependencies |
| `build.gradle` | Java | Gradle dependencies |
| `Gemfile` | Ruby | Bundler dependencies |
| `composer.json` | PHP | Composer dependencies |

### Framework Detection

| File Pattern | Framework |
|--------------|-----------|
| `next.config.js` | Next.js |
| `nuxt.config.js` | Nuxt.js |
| `vue.config.js` | Vue CLI |
| `angular.json` | Angular |
| `svelte.config.js` | Svelte |
| `remix.config.js` | Remix |
| `astro.config.mjs` | Astro |
| `wrangler.toml` | Cloudflare Workers |
| `vercel.json` | Vercel |
| `netlify.toml` | Netlify |
| `serverless.yml` | Serverless Framework |
| `sam.yaml` | AWS SAM |
| `terraform/` | Terraform |

### Database Detection

| File/Pattern | Database |
|--------------|----------|
| `prisma/schema.prisma` | Prisma (PostgreSQL, MySQL, SQLite) |
| `schema.sql` | SQL database |
| `migrations/` | Database migrations |
| `docker-compose.yml` with mongo | MongoDB |
| `docker-compose.yml` with redis | Redis |
| `wrangler.toml` with d1_databases | Cloudflare D1 |
| `wrangler.toml` with kv_namespaces | Cloudflare KV |

## Code Pattern Recognition

### API Endpoint Patterns

**Express.js:**
```javascript
app.get('/api/users', handler)
app.post('/api/users', handler)
router.get('/users', handler)
```

**FastAPI:**
```python
@app.get("/api/users")
@app.post("/api/users")
router = APIRouter()
```

**Go (net/http):**
```go
http.HandleFunc("/api/users", handler)
mux.HandleFunc("/api/users", handler)
```

**Rust (actix-web):**
```rust
.route("/api/users", web::get().to(handler))
.route("/api/users", web::post().to(handler))
```

### Authentication Patterns

**JWT:**
- Look for `jsonwebtoken`, `jwt`, `jose` imports
- Check for token generation/validation functions

**Session:**
- Look for `express-session`, `cookie-session`
- Check for session middleware

**OAuth:**
- Look for `passport`, `auth0`, `firebase auth`
- Check for OAuth provider configuration

### Middleware Patterns

**Express.js:**
```javascript
app.use(middleware)
router.use(middleware)
```

**FastAPI:**
```python
app.add_middleware(MiddlewareClass)
@app.middleware("http")
```

**Go:**
```go
func middleware(next http.Handler) http.Handler
```

## Dependency Analysis

### Security-Related Dependencies

| Category | Packages |
|----------|----------|
| Auth | `jsonwebtoken`, `passport`, `auth0`, `firebase-admin` |
| Validation | `joi`, `zod`, `yup`, `validator.js` |
| Security | `helmet`, `cors`, `rate-limiter` |
| Encryption | `bcrypt`, `crypto-js`, `argon2` |

### Testing Dependencies

| Category | Packages |
|----------|----------|
| Unit | `jest`, `vitest`, `mocha`, `pytest` |
| E2E | `playwright`, `cypress`, `selenium` |
| Coverage | `nyc`, `coverage.py`, `tarpaulin` |

### Performance Dependencies

| Category | Packages |
|----------|----------|
| Caching | `redis`, `memcached`, `lru-cache` |
| Queue | `bull`, `rabbitmq`, `kafka` |
| Monitoring | `newrelic`, `datadog`, `sentry` |

## Architecture Pattern Indicators

### Serverless

- `wrangler.toml` - Cloudflare Workers
- `vercel.json` or `api/` directory - Vercel Functions
- `netlify.toml` or `netlify/functions/` - Netlify Functions
- `serverless.yml` - Serverless Framework
- `template.yaml` - AWS SAM

### Microservices

- Multiple `Dockerfile` files
- `docker-compose.yml` with multiple services
- API gateway configuration
- Service discovery configuration

### Monolith

- Single entry point
- All code in one directory structure
- Single database connection

### SPA (Single Page Application)

- Frontend framework in dependencies
- API calls to external/backend services
- Client-side routing
