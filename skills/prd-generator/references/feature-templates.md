# Feature Templates

## Authentication & Authorization

### User Authentication
```markdown
### Feature: User Authentication

**User Stories:**
- As a new user, I want to register an account so that I can access personalized features.
- As a registered user, I want to log in so that I can access my account.
- As a user, I want to log out so that I can secure my account.

**Acceptance Criteria:**
- Registration with email/password
- Email verification
- Password reset functionality
- Session management
- Secure password storage (bcrypt/argon2)

**Technical Notes:**
- Implement JWT or session-based auth
- Add rate limiting on auth endpoints
- Store passwords hashed, never plain text
```

### OAuth Integration
```markdown
### Feature: OAuth Integration

**User Stories:**
- As a user, I want to log in with Google so that I can access the app quickly.
- As a user, I want to log in with GitHub so that I can use my developer account.

**Acceptance Criteria:**
- Support major providers (Google, GitHub, etc.)
- Account linking for existing users
- Secure token handling

**Technical Notes:**
- Use passport.js or similar
- Store provider IDs securely
- Handle token refresh
```

### Role-Based Access Control
```markdown
### Feature: Role-Based Access Control (RBAC)

**User Stories:**
- As an admin, I want to manage user roles so that I can control access.
- As a user, I want to only see features I have permission for.

**Acceptance Criteria:**
- Define roles (admin, user, moderator)
- Permission-based feature access
- Role assignment interface

**Technical Notes:**
- Store roles in database
- Middleware for route protection
- UI conditional rendering
```

## API Features

### Rate Limiting
```markdown
### Feature: Rate Limiting

**User Stories:**
- As an API provider, I want to limit requests so that the service remains available.
- As a legitimate user, I want to know my rate limit status.

**Acceptance Criteria:**
- Configurable rate limits per endpoint
- Rate limit headers in response
- Graceful limit exceeded response

**Technical Notes:**
- Use sliding window or token bucket
- Store counters in Redis or memory
- Include Retry-After header
```

### API Documentation
```markdown
### Feature: API Documentation

**User Stories:**
- As a developer, I want to read API docs so that I can integrate correctly.
- As a developer, I want to try API endpoints interactively.

**Acceptance Criteria:**
- OpenAPI/Swagger specification
- Interactive documentation UI
- Code examples in multiple languages

**Technical Notes:**
- Generate from code annotations
- Keep docs in sync with implementation
- Version documentation
```

### API Versioning
```markdown
### Feature: API Versioning

**User Stories:**
- As an API consumer, I want stable API versions so that my integration doesn't break.
- As an API provider, I want to deprecate old versions gracefully.

**Acceptance Criteria:**
- URL or header-based versioning
- Version in response headers
- Deprecation notices
- Migration guides

**Technical Notes:**
- Support at least 2 versions simultaneously
- Clear deprecation timeline
- Version in route path: /v1/, /v2/
```

## User Experience

### Internationalization (i18n)
```markdown
### Feature: Internationalization

**User Stories:**
- As a non-English user, I want the app in my language so that I can use it effectively.
- As a user, I want to switch languages easily.

**Acceptance Criteria:**
- Support multiple languages
- Language selector in UI
- Date/number formatting by locale
- RTL support for applicable languages

**Technical Notes:**
- Use i18next, react-intl, or similar
- Store translations in JSON files
- Detect browser language
```

### Accessibility (a11y)
```markdown
### Feature: Accessibility

**User Stories:**
- As a screen reader user, I want to navigate the app effectively.
- As a keyboard-only user, I want to use all features without a mouse.

**Acceptance Criteria:**
- WCAG 2.1 AA compliance
- Proper heading hierarchy
- Alt text for images
- Focus management
- Color contrast ratios met

**Technical Notes:**
- Use semantic HTML
- ARIA labels where needed
- Test with screen readers
```

### Dark Mode
```markdown
### Feature: Dark Mode

**User Stories:**
- As a user, I want a dark theme so that I can reduce eye strain.
- As a user, I want the app to follow my system preference.

**Acceptance Criteria:**
- Light and dark themes
- System preference detection
- Manual toggle
- Persist preference

**Technical Notes:**
- CSS custom properties
- prefers-color-scheme media query
- Store preference in localStorage
```

## Data & Storage

### Search Functionality
```markdown
### Feature: Search

**User Stories:**
- As a user, I want to search content so that I can find specific items.
- As a user, I want filtered results so that I can narrow down results.

**Acceptance Criteria:**
- Full-text search
- Filters and facets
- Search suggestions
- Highlighted results

**Technical Notes:**
- Use database full-text search or Elasticsearch
- Implement debouncing
- Cache frequent queries
```

### Data Export
```markdown
### Feature: Data Export

**User Stories:**
- As a user, I want to export my data so that I have a backup.
- As a user, I want to export in multiple formats.

**Acceptance Criteria:**
- Export to CSV, JSON
- Select data range
- Email large exports
- Include all user data

**Technical Notes:**
- Stream large exports
- Background job for large files
- Secure download links
```

## DevOps & Monitoring

### Health Checks
```markdown
### Feature: Health Checks

**User Stories:**
- As an operator, I want to check service health so that I can monitor uptime.
- As a load balancer, I want to detect unhealthy instances.

**Acceptance Criteria:**
- /health endpoint
- Database connectivity check
- External service status
- Detailed status codes

**Technical Notes:**
- Return 200 for healthy, 503 for unhealthy
- Include version and uptime
- Check critical dependencies
```

### Logging
```markdown
### Feature: Structured Logging

**User Stories:**
- As a developer, I want structured logs so that I can search and analyze them.
- As an operator, I want to trace requests across services.

**Acceptance Criteria:**
- JSON structured logs
- Request ID tracking
- Log levels (debug, info, warn, error)
- Sensitive data redaction

**Technical Notes:**
- Use winston, pino, or similar
- Include context in each log
- Correlate logs with request ID
```

### Error Tracking
```markdown
### Feature: Error Tracking

**User Stories:**
- As a developer, I want to be notified of errors so that I can fix them.
- As a developer, I want error context so that I can reproduce issues.

**Acceptance Criteria:**
- Automatic error capture
- Error grouping
- Source map support
- User impact metrics

**Technical Notes:**
- Integrate Sentry, Bugsnag, or similar
- Include stack traces
- Track error frequency
```

## Security

### Input Validation
```markdown
### Feature: Input Validation

**User Stories:**
- As a user, I want clear error messages when my input is invalid.
- As a system, I want to reject malicious input.

**Acceptance Criteria:**
- Validate all user input
- Sanitize for XSS
- SQL injection prevention
- Clear error messages

**Technical Notes:**
- Use validation library (joi, zod, yup)
- Parameterized queries
- Content Security Policy
```

### CORS Configuration
```markdown
### Feature: CORS Configuration

**User Stories:**
- As an API provider, I want to control which origins can access my API.
- As a frontend developer, I want to make cross-origin requests securely.

**Acceptance Criteria:**
- Explicit allowed origins
- Credentials support if needed
- Preflight handling
- Environment-specific config

**Technical Notes:**
- Never use * in production
- List specific domains
- Handle OPTIONS requests
```

### Secret Management
```markdown
### Feature: Secret Management

**User Stories:**
- As a developer, I want secrets secured so that the application is safe.
- As an operator, I want to rotate secrets without code changes.

**Acceptance Criteria:**
- No secrets in code
- Environment variable injection
- Secret rotation support
- Audit logging

**Technical Notes:**
- Use vault or cloud secret managers
- Never log secrets
- Rotate keys regularly
```

## Performance

### Caching
```markdown
### Feature: Caching

**User Stories:**
- As a user, I want fast page loads so that I have a good experience.
- As a system, I want to reduce database load.

**Acceptance Criteria:**
- Cache static assets
- Cache API responses where appropriate
- Cache invalidation strategy
- Cache hit metrics

**Technical Notes:**
- Use Redis or in-memory cache
- Set appropriate TTLs
- Implement cache headers
```

### Lazy Loading
```markdown
### Feature: Lazy Loading

**User Stories:**
- As a user, I want fast initial page load.
- As a user, I want content to load as I need it.

**Acceptance Criteria:**
- Lazy load images
- Lazy load components
- Loading placeholders
- Progressive enhancement

**Technical Notes:**
- Use Intersection Observer
- Code splitting
- Skeleton screens
```
