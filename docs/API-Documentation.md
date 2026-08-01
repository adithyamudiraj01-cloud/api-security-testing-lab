# API Documentation

## Base URL

```
http://127.0.0.1:5000
```

---

# 1. Home API

### Endpoint

```
GET /
```

### Description

Returns the welcome message.

---

# 2. Register API

### Endpoint

```
POST /register
```

### Request Body

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "123456"
}
```

### Response

```json
{
  "message": "Registration Successful"
}
```

---

# 3. Login API

### Endpoint

```
POST /login
```

### Request Body

```json
{
  "email": "john@example.com",
  "password": "123456"
}
```

### Response

```json
{
  "token": "<JWT_TOKEN>"
}
```

---

# 4. Profile API

### Endpoint

```
GET /profile
```

### Headers

```
Authorization: Bearer <JWT_TOKEN>
```

### Response

Returns the authenticated user's profile.

---

# 5. Account API

### Endpoint

```
GET /account/<user_id>
```

### Headers

```
Authorization: Bearer <JWT_TOKEN>
```

### Description

Returns account details only if the requested user ID belongs to the authenticated user.

---

# 6. Transfer API

### Endpoint

```
POST /transfer
```

### Request Body

```json
{
  "from_account": "1001",
  "to_account": "1002",
  "amount": 500
}
```

### Response

```json
{
  "message": "Transfer Successful"
}
```

---

# 7. API Key Protected API

### Endpoint

```
GET /api/data
```

### Headers

```
X-API-Key: labmentix-api-key-123
```

### Success Response

```json
{
  "message": "API Key Verified",
  "data": [
    "Cyber Security",
    "API Testing",
    "Burp Suite"
  ]
}
```

### Failure Response

```json
{
  "message": "Invalid or Missing API Key"
}
```

---

# Authentication

Protected endpoints require a valid JWT:

```
Authorization: Bearer <JWT_TOKEN>
```

---

# API Key Authentication

The `/api/data` endpoint requires the following header:

```
X-API-Key: labmentix-api-key-123
```

API keys supplied through URL query parameters are rejected.

---

# Security Features

- JWT Authentication
- Object Level Authorization (BOLA)
- Mass Assignment Protection
- Parameter Tampering Protection
- API Key Authentication
- API Key Exposure Prevention
- Rate Limiting
- Security Headers