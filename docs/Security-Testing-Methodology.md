# Security Testing Methodology

## 1. Introduction

This document describes the methodology used to test the security of the API Security Testing Lab.

The testing was performed against a locally hosted Flask API using Postman and Burp Suite.

## 2. Testing Objective

The main objectives were:

- Identify API authentication weaknesses.
- Test authorization controls.
- Identify Broken Object Level Authorization (BOLA).
- Test for Mass Assignment.
- Test for Parameter Tampering.
- Test JWT authentication.
- Test invalid or modified JWT tokens.
- Perform SQL-injection-style input testing.
- Test rate limiting.
- Verify security headers.
- Intercept and modify requests using Burp Suite.
- Verify that security fixes prevent the identified attacks.

## 3. Testing Environment

### Application

Flask-based REST API running locally.

### Base URL

http://127.0.0.1:5000

### Tools

- Python 3.11
- Flask
- Visual Studio Code
- Postman
- Burp Suite
- JSON file storage

## 4. Testing Method

The following general process was used:

1. Start the Flask application.
2. Send normal requests using Postman.
3. Observe the normal response.
4. Modify request parameters or authentication information.
5. Send the modified request.
6. Analyze the response.
7. Identify the security issue.
8. Implement a security control.
9. Repeat the test.
10. Compare the vulnerable and fixed behavior.
11. Capture screenshots as evidence.

## 5. BOLA / IDOR Testing

### Objective

To determine whether one authenticated user can access another user's account by changing the object ID.

### Normal Request

GET /account/1

A JWT belonging to User 1 was used.

### Attack Request

GET /account/2

The JWT was kept unchanged while only the account ID was modified.

### Vulnerable Behavior

The vulnerable implementation allowed access to another user's account.

### Remediation

The API compares the requested account ID with the authenticated user's ID extracted from the JWT.

### Secure Behavior

User 1 can access:

GET /account/1

User 1 cannot access:

GET /account/2

The unauthorized request returns:

403 Forbidden

## 6. Mass Assignment Testing

### Objective

To determine whether a user can add unauthorized properties to a registration request.

### Test Request

POST /register

```json
{
    "username": "attacker",
    "email": "attacker@example.com",
    "password": "123456",
    "role": "admin",
    "isAdmin": true
}