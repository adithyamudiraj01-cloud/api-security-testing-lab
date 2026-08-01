# 🔐 API Security Testing Lab

A beginner-friendly API Security Testing Lab built using Flask, Postman, and Burp Suite.

This project demonstrates how common API vulnerabilities are identified, tested, and mitigated using practical examples.

---

# Features

- User Registration API
- User Login API
- JWT Authentication
- Protected Profile API
- Account Authorization
- Rate Limiting
- Security Headers
- API Documentation
- Burp Suite Testing
- Postman Collection

---

# Technologies Used

- Python 3.11
- Flask
- JWT
- Flask-Limiter
- Flask-CORS
- JSON Storage
- Postman
- Burp Suite
- Visual Studio Code

---

# Project Structure

```
api-testing-tool/
│
├── backend/
├── docs/
├── frontend/
├── postman/
├── report/
└── screenshots/
```

---

# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home API |
| POST | /register | Register User |
| POST | /login | Login User |
| GET | /profile | Protected Profile |
| GET | /account/<id> | Account Details |
| POST | /transfer | Money Transfer |

---

# Security Tests

- Broken Object Level Authorization (BOLA)
- Mass Assignment
- Parameter Tampering
- JWT Tampering
- Invalid JWT
- Rate Limiting
- Security Headers
- Burp Suite Request Interception

---

# Screenshots

All testing screenshots are available in the **screenshots** folder.

---

# Educational Purpose

This project was developed for learning API Security concepts and should not be used in production.

---

# Author

Neela Adithya