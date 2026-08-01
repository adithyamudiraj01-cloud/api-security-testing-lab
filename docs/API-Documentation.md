# API Documentation

## Base URL

```text
http://127.0.0.1:5000

## Home API

Method: GET

URL:
http://127.0.0.1:5000/

Description:
Checks whether the API is running.
## Register API

Method: POST

URL:
http://127.0.0.1:5000/register

Request Body:

{
    "username": "example",
    "email": "example@gmail.com",
    "password": "123456"
}
## Register API

Method: POST

URL:
http://127.0.0.1:5000/register

Description:
Creates a new user account.

Request Body:

{
    "username": "example",
    "email": "example@gmail.com",
    "password": "123456"
}

Expected Response:

{
    "message": "Registration Successful",
    "user": {
        "id": 1,
        "username": "example",
        "email": "example@gmail.com",
        "password": "123456"
    }
}

## Login API

Method: POST

URL:
http://127.0.0.1:5000/login

Description:
Authenticates a registered user and returns a JWT token.

Request Body:

{
    "email": "adithya@gmail.com",
    "password": "123456"
}

Expected Response:

{
    "message": "Login Successful",
    "token": "<JWT_TOKEN>"
}

## Profile API

Method: GET

URL:
http://127.0.0.1:5000/profile

Description:
Returns information for the authenticated user.

Authentication:
Bearer JWT token is required.

Authorization Header:

Authorization: Bearer <JWT_TOKEN>

Expected Response:

{
    "message": "Profile details",
    "user": {
        "id": 1,
        "username": "Adithya_New",
        "email": "adithya@gmail.com"
    }
}

## Account API

Method: GET

URL:
http://127.0.0.1:5000/account/<user_id>

Example:
http://127.0.0.1:5000/account/1

Description:
Returns account information for the authenticated user.

Authentication:
Bearer JWT token is required.

Authorization:
The authenticated user can access only their own account.

Expected Response for Authorized User:

{
    "id": 1,
    "username": "Adithya_New",
    "email": "adithya@gmail.com"
}

BOLA Protection:
If User 1 attempts to access /account/2, the server returns:

{
    "message": "Forbidden"
}

HTTP Status:
403 Forbidden

## Transfer API

Method: POST

URL:
http://127.0.0.1:5000/transfer

Description:
Simulates a transfer between two accounts.

Request Body:

{
    "from_account": "1001",
    "to_account": "1002",
    "amount": 500
}

Expected Response:

{
    "from_account": "1001",
    "to_account": "1002",
    "amount": 500,
    "message": "Transfer Successful"
}

Security Control:
The server verifies that the requested source account belongs to the authenticated user.

Parameter Tampering Test:

A tampered request such as:

{
    "from_account": "9999",
    "to_account": "1002",
    "amount": 1
}

is rejected.

Expected Response:

{
    "message": "Forbidden: You cannot transfer from this account"
}

HTTP Status:
403 Forbidden

## Mass Assignment Testing

Endpoint:
POST /register

Description:
Tests whether the API accepts unauthorized fields supplied by the client.

Vulnerable Test Request:

{
    "username": "attacker",
    "email": "attacker@example.com",
    "password": "123456",
    "role": "admin",
    "isAdmin": true
}

Vulnerability:
In the vulnerable implementation, unexpected fields such as "role" and "isAdmin" could be stored.

Remediation:
The secure implementation allows only:
- username
- email
- password

Expected Secure Behavior:
The "role" and "isAdmin" fields are ignored and are not stored.

Result:
Mass Assignment vulnerability fixed.
## SQL Injection Testing

Endpoint:
POST /search

Description:
Tests whether user-supplied input is safely handled and whether SQL injection can affect the application.

Test Payload:

{
    "username": "' OR '1'='1"
}

Expected Secure Behavior:
The application should not execute the input as SQL or return unauthorized records.

Expected Result:

{
    "results": []
}

Result:
SQL Injection test completed successfully.
## Rate Limiting

Endpoint:
POST /login

Description:
Limits repeated login attempts to help prevent brute-force attacks.

Test Request:

{
    "email": "adithya@gmail.com",
    "password": "wrongpassword"
}

Expected Behavior:

The first few failed attempts return:

401 Unauthorized

After the configured request limit is exceeded:

429 Too Many Requests

Result:
Rate limiting prevents excessive repeated login attempts.
## Security Headers

Endpoint:
GET /

Description:
Checks whether recommended HTTP security headers are included in API responses.

Headers Checked:

X-Content-Type-Options: nosniff

X-Frame-Options: DENY

X-XSS-Protection: 1; mode=block

Expected Result:
Security headers should be present in the HTTP response.

Purpose:
These headers provide additional protection against certain browser-based attacks and unsafe content handling.

Result:
Security headers were verified in the API response.
