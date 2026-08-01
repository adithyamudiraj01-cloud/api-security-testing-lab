# Security Testing Methodology

## Objective

The objective of this project is to evaluate the security of a REST API by identifying, testing, and mitigating common API vulnerabilities.

---

## Testing Environment

- Python 3.11
- Flask
- Visual Studio Code
- Postman
- Burp Suite
- JSON File Storage

---

## Security Tests Performed

### 1. Broken Object Level Authorization (BOLA)

Verified that authenticated users cannot access resources belonging to other users.

---

### 2. JWT Authentication Testing

Verified that protected endpoints require a valid JWT token.

---

### 3. JWT Tampering

Modified a valid JWT and verified that the server rejected the altered token.

---

### 4. Mass Assignment

Attempted to submit unauthorized fields such as `role` and `isAdmin` during user registration.

---

### 5. Parameter Tampering

Modified transaction parameters (`from_account`, `to_account`, and `amount`) to verify server-side authorization.

---

### 6. API Key Authentication

Implemented an endpoint protected by an API key passed through the `X-API-Key` request header.

---

### 7. API Key Exposure Testing

Verified that API keys supplied as URL query parameters were rejected. Only API keys sent in the `X-API-Key` header were accepted.

---

### 8. Rate Limiting

Verified that repeated login attempts were limited to reduce brute-force attacks.

---

### 9. Security Headers

Verified the presence of the following HTTP security headers:

- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- X-XSS-Protection: 1; mode=block

---

## Tools Used

- Postman
- Burp Suite
- Flask
- Python
- JWT

---

## Conclusion

The API was tested against common security risks including authentication, authorization, request manipulation, API key handling, and rate limiting. The implemented security controls successfully mitigated the tested vulnerabilities.