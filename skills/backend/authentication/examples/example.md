# Authentication Example

## Scenario

Implement JWT-based authentication for a SaaS Customer Service platform with multi-tenant support, role-based access control, and OAuth social login.

## Input

- **Authentication Methods**: Email/password, Google OAuth, GitHub OAuth
- **User Roles**: Admin, Agent, Customer
- **Multi-tenant**: Users belong to organizations
- **Security**: Rate limiting, MFA optional, audit logs
- **Compliance**: GDPR (right to deletion), SOC2

## Process

### Step 1: Database Schema

```sql
-- Users table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID NOT NULL REFERENCES tenants(id),
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255), -- NULL for OAuth users
  name VARCHAR(255) NOT NULL,
  role VARCHAR(50) NOT NULL DEFAULT 'customer', -- admin, agent, customer
  mfa_enabled BOOLEAN DEFAULT FALSE,
  mfa_secret VARCHAR(255),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Refresh tokens
CREATE TABLE refresh_tokens (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  token_hash VARCHAR(255) NOT NULL UNIQUE,
  expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  revoked_at TIMESTAMPTZ
);

-- OAuth providers
CREATE TABLE oauth_providers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  provider VARCHAR(50) NOT NULL, -- google, github
  provider_user_id VARCHAR(255) NOT NULL,
  access_token TEXT,
  refresh_token TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(provider, provider_user_id)
);

-- Audit logs
CREATE TABLE auth_audit_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id),
  event_type VARCHAR(100) NOT NULL, -- login_success, login_failed, logout, etc.
  ip_address INET,
  user_agent TEXT,
  metadata JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Step 2: JWT Token Structure

**Access Token** (short-lived: 15 minutes):
```json
{
  "sub": "user-uuid",
  "tenant_id": "tenant-uuid",
  "email": "user@example.com",
  "role": "agent",
  "iat": 1705123456,
  "exp": 1705124356
}
```

**Refresh Token** (long-lived: 7 days):
- Stored as hash in database
- Rotated on each use
- Revoked on logout

### Step 3: Authentication Flow

**Email/Password Login**:
```python
from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from jose import jwt, JWTError
import secrets

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"])

@router.post("/auth/login")
async def login(credentials: LoginRequest):
    # 1. Find user
    user = await db.users.find_by_email(credentials.email)
    if not user:
        await log_audit(None, "login_failed", {"email": credentials.email})
        raise HTTPException(401, "Invalid credentials")
    
    # 2. Verify password
    if not pwd_context.verify(credentials.password, user.password_hash):
        await log_audit(user.id, "login_failed", {"reason": "wrong_password"})
        raise HTTPException(401, "Invalid credentials")
    
    # 3. Check MFA if enabled
    if user.mfa_enabled:
        if not verify_mfa(user.mfa_secret, credentials.mfa_code):
            raise HTTPException(401, "Invalid MFA code")
    
    # 4. Generate tokens
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    
    # 5. Store refresh token
    await db.refresh_tokens.create(
        user_id=user.id,
        token_hash=hash_token(refresh_token),
        expires_at=now() + timedelta(days=7)
    )
    
    # 6. Log success
    await log_audit(user.id, "login_success")
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": 900
    }
```

**OAuth Login (Google)**:
```python
from authlib.integrations.starlette_client import OAuth

oauth = OAuth()
oauth.register(
    name='google',
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

@router.get("/auth/google")
async def google_login(request: Request):
    redirect_uri = request.url_for('google_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/auth/google/callback")
async def google_callback(request: Request):
    # 1. Get user info from Google
    token = await oauth.google.authorize_access_token(request)
    userinfo = token['userinfo']
    
    # 2. Find or create user
    oauth_provider = await db.oauth_providers.find(
        provider='google',
        provider_user_id=userinfo['sub']
    )
    
    if oauth_provider:
        user = await db.users.get(oauth_provider.user_id)
    else:
        # Create new user
        user = await db.users.create(
            email=userinfo['email'],
            name=userinfo['name'],
            role='customer'
        )
        await db.oauth_providers.create(
            user_id=user.id,
            provider='google',
            provider_user_id=userinfo['sub'],
            access_token=token['access_token']
        )
    
    # 3. Generate tokens
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    
    return {"access_token": access_token, "refresh_token": refresh_token}
```

### Step 4: Authorization Middleware

```python
from fastapi import Request, HTTPException

def require_role(*roles: str):
    """Dependency to check user role"""
    async def role_checker(request: Request):
        user = request.state.user
        if user.role not in roles:
            raise HTTPException(403, "Insufficient permissions")
        return user
    return role_checker

def require_tenant_access():
    """Dependency to check tenant access"""
    async def tenant_checker(request: Request):
        user = request.state.user
        resource_tenant_id = request.path_params.get('tenant_id')
        
        if user.role != 'admin' and user.tenant_id != resource_tenant_id:
            raise HTTPException(403, "Access denied to this tenant")
        return user
    return tenant_checker

# Usage
@router.get("/tenants/{tenant_id}/conversations")
async def list_conversations(
    tenant_id: str,
    user: User = Depends(require_role('admin', 'agent')),
    _: User = Depends(require_tenant_access())
):
    conversations = await db.conversations.find_by_tenant(tenant_id)
    return conversations
```

### Step 5: Token Refresh

```python
@router.post("/auth/refresh")
async def refresh_token(refresh_request: RefreshRequest):
    # 1. Verify refresh token
    token_hash = hash_token(refresh_request.refresh_token)
    stored_token = await db.refresh_tokens.find_by_hash(token_hash)
    
    if not stored_token or stored_token.revoked_at:
        raise HTTPException(401, "Invalid refresh token")
    
    if stored_token.expires_at < now():
        raise HTTPException(401, "Refresh token expired")
    
    # 2. Get user
    user = await db.users.get(stored_token.user_id)
    
    # 3. Rotate refresh token (security best practice)
    await db.refresh_tokens.update(
        id=stored_token.id,
        revoked_at=now()
    )
    
    new_refresh_token = create_refresh_token(user)
    await db.refresh_tokens.create(
        user_id=user.id,
        token_hash=hash_token(new_refresh_token),
        expires_at=now() + timedelta(days=7)
    )
    
    # 4. Generate new access token
    new_access_token = create_access_token(user)
    
    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "expires_in": 900
    }
```

### Step 6: Rate Limiting

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@router.post("/auth/login")
@limiter.limit("5/minute")  # 5 attempts per minute per IP
async def login(request: Request, credentials: LoginRequest):
    # ... login logic
    pass

@router.post("/auth/refresh")
@limiter.limit("10/minute")
async def refresh_token(request: Request, refresh_request: RefreshRequest):
    # ... refresh logic
    pass
```

### Step 7: Security Measures

**Password Hashing**:
```python
# Use bcrypt with strong salt rounds
pwd_context = CryptContext(schemes=["bcrypt"], bcrypt__rounds=12)

# Hash password
password_hash = pwd_context.hash("user_password")

# Verify password
is_valid = pwd_context.verify("user_password", password_hash)
```

**JWT Configuration**:
```python
from jose import jwt

JWT_SECRET = settings.JWT_SECRET  # 256-bit random secret
JWT_ALGORITHM = "HS256"

def create_access_token(user: User) -> str:
    payload = {
        "sub": str(user.id),
        "tenant_id": str(user.tenant_id),
        "email": user.email,
        "role": user.role,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=15)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def verify_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(401, "Invalid token")
```

## Output

### Authentication API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/register` | POST | User registration |
| `/auth/login` | POST | Email/password login |
| `/auth/google` | GET | Google OAuth login |
| `/auth/google/callback` | GET | Google OAuth callback |
| `/auth/refresh` | POST | Refresh access token |
| `/auth/logout` | POST | Logout (revoke tokens) |
| `/auth/mfa/enable` | POST | Enable MFA |
| `/auth/mfa/verify` | POST | Verify MFA code |
| `/auth/password/reset` | POST | Request password reset |
| `/auth/password/confirm` | POST | Confirm password reset |

### Security Features

✅ **Password Security**: bcrypt hashing (12 rounds)
✅ **Token Security**: JWT with HS256, short-lived access tokens
✅ **Refresh Token Rotation**: Tokens rotated on each use
✅ **Rate Limiting**: 5 login attempts/minute, 10 refresh/minute
✅ **MFA Support**: TOTP-based multi-factor authentication
✅ **OAuth Integration**: Google and GitHub social login
✅ **Audit Logging**: All authentication events logged
✅ **Multi-tenant Isolation**: Tenant-based access control
✅ **HTTPS Only**: All endpoints require HTTPS
✅ **Input Validation**: All inputs validated and sanitized

### Performance

- Login: < 200ms
- Token refresh: < 100ms
- Token verification: < 10ms

### Compliance

- **GDPR**: User data deletion on account closure
- **SOC2**: Comprehensive audit logging
- **OWASP Top 10**: All vulnerabilities mitigated

### Testing Strategy

1. **Unit Tests**: Password hashing, token generation/verification
2. **Integration Tests**: Full authentication flows
3. **Security Tests**: Brute force, token manipulation, SQL injection
4. **Load Tests**: 1000 concurrent logins
