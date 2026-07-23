# Authentication Skill

## Goal

Design and implement secure, scalable authentication and authorization systems that protect user data and comply with security standards.

## When To Use

- Implementing user authentication from scratch
- Adding OAuth/social login providers
- Designing role-based access control (RBAC)
- Implementing multi-factor authentication (MFA)
- Securing API endpoints
- Handling session management
- Implementing token-based authentication (JWT)

## Workflow

### Step 1

Analyze authentication requirements.

Identify:
- Authentication methods needed (password, OAuth, SSO, MFA)
- User types and roles
- Session management requirements
- Compliance requirements (GDPR, HIPAA, SOC2)
- Security threat model

### Step 2

Choose authentication strategy.

Evaluate:
- **Password-based**: Traditional, requires secure storage
- **OAuth 2.0**: Social login, third-party integration
- **JWT tokens**: Stateless, scalable, API-friendly
- **Session-based**: Server-side, traditional web apps
- **Multi-factor**: SMS, email, authenticator apps, hardware keys
- **Single Sign-On (SSO)**: Enterprise, SAML, OIDC

### Step 3

Design authentication flow.

Implement:
- User registration flow
- Login flow (with MFA if required)
- Password reset flow
- Session management (creation, refresh, revocation)
- Logout flow (invalidate tokens/sessions)

### Step 4

Design authorization model.

Define:
- Roles and permissions
- Role hierarchy (admin > manager > user)
- Resource-based access control
- API endpoint protection
- Middleware/interceptors for authorization checks

### Step 5

Implement security measures.

Include:
- Password hashing (bcrypt, Argon2)
- Token signing and validation
- Rate limiting (brute force protection)
- CSRF protection
- XSS prevention
- SQL injection prevention
- Input validation and sanitization

### Step 6

Design session and token management.

Plan:
- Access token lifetime (short: 15min-1hr)
- Refresh token lifetime (long: 7-30 days)
- Token storage (HTTP-only cookies, secure storage)
- Token revocation strategy
- Session invalidation on logout

### Step 7

Implement monitoring and logging.

Track:
- Failed login attempts
- Successful logins
- Token refresh events
- Permission denied events
- Suspicious activity patterns

### Step 8

Document authentication system.

Create:
- Authentication flow diagrams
- API documentation (endpoints, request/response)
- Security best practices
- Integration guides
- Troubleshooting guide

## Rules

1. Never store passwords in plain text—always hash.
2. Use industry-standard libraries (don't roll your own crypto).
3. Implement rate limiting to prevent brute force attacks.
4. Use HTTPS for all authentication endpoints.
5. Validate and sanitize all user inputs.
6. Log authentication events for security monitoring.
7. Implement proper error handling (don't leak information).
8. Regularly rotate secrets and API keys.

## Output

- Authentication flow diagrams
- Authorization model documentation
- API endpoint specifications
- Security implementation details
- Integration guides
- Testing strategy
- Monitoring and logging plan

## Quality Criteria

- All passwords securely hashed and stored
- Tokens properly signed and validated
- Authorization checks on all protected endpoints
- Rate limiting prevents brute force attacks
- Session management is secure and efficient
- Comprehensive logging and monitoring
- Security vulnerabilities identified and mitigated
- Compliance requirements met
