# API Security Testing Report

## 1. Executive Summary

This report documents the security testing performed on the API Security Testing Lab.

The application was developed using Flask and tested locally using Postman and Burp Suite.

The testing focused on authentication, authorization, input validation, and common API security weaknesses.

## 2. Scope

The following API functionality was tested:

- User registration
- User login
- JWT authentication
- Profile access
- Account access
- User updates
- Account transfers

## 3. Testing Tools

- Python 3.11
- Flask
- Postman
- Burp Suite
- Visual Studio Code

## 4. Security Tests Performed

### 4.1 Broken Object Level Authorization (BOLA)

A User 1 JWT was used to request User 2's account:

GET /account/2

Expected secure result:

403 Forbidden

The API verifies that the requested object belongs to the authenticated user.

### 4.2 Mass Assignment

The registration endpoint was tested with additional fields:

```json
{
    "username": "attacker",
    "email": "attacker@example.com",
    "password": "123456",
    "role": "admin",
    "isAdmin": true
}
Vulnerability

The test attempted to submit unauthorized fields such as role and isAdmin.

Remediation

The secure implementation explicitly accepts only the approved registration fields:

username
email
password
Secure Result

Unauthorized fields such as role and isAdmin are not stored as user-controlled attributes.

4.3 Parameter Tampering
Objective

To determine whether sensitive transaction parameters can be modified by the client.

Test Request

POST /transfer

{
    "from_account": "9999",
    "to_account": "1002",
    "amount": 1
}
Vulnerability

The test attempted to change the source account to an account that did not belong to the authenticated user.

Secure Result

The request was rejected with:

403 Forbidden

Remediation

The server validates the source account against the authenticated user before allowing the transfer.

4.4 JWT Tampering
Objective

To determine whether modified JWT tokens are accepted by protected endpoints.

Test

A valid JWT was obtained through the Login API.

The JWT was then modified by changing one character using Burp Suite.

The modified token was sent to a protected endpoint.

Secure Result

The API rejected the modified token with:

401 Unauthorized

Remediation

The API verifies the JWT signature and rejects invalid or modified tokens.

4.5 SQL-Injection-Style Input Testing
Objective

To test whether SQL-injection-style input is safely handled.

Test Input
' OR '1'='1
Result

The application uses JSON-file storage rather than a SQL database.

Therefore, this was treated as an input-handling test rather than a test against an actual SQL query.

The application should not interpret the input as executable SQL or return unauthorized records.

4.6 Rate Limiting
Objective

To determine whether repeated login attempts are restricted.

Test

Multiple unsuccessful login requests were sent to:

POST /login

using an incorrect password.

Result

After the request limit was exceeded, the API returned:

429 Too Many Requests

Security Purpose

Rate limiting helps reduce repeated brute-force login attempts.

4.7 Security Headers
Objective

To verify security-related HTTP response headers.

Headers Verified
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Result

The above headers were observed in the API response.

These headers provide additional protection against certain browser-related security issues.

5. Authentication Testing
5.1 Valid JWT

A valid user login was performed using the Login API.

The returned JWT was used to access the protected Profile API.

Result

The authenticated request was accepted successfully.

5.2 Invalid JWT

A valid JWT was modified and then submitted to the protected Profile API.

Result

The API rejected the modified token with:

401 Unauthorized

6. Burp Suite Testing

Burp Suite was configured as an interception proxy between Postman and the local Flask API.

Tests Performed
Login request interception
Password tampering
JWT tampering
Object ID tampering
Method
Start Burp Suite.
Start the proxy listener.
Configure Postman to use the Burp proxy.
Enable interception.
Send the request from Postman.
Capture the request in Burp Suite.
Modify selected request parameters.
Forward the modified request.
Analyze the server response.
7. Security Controls

The following security controls were implemented or verified:

JWT-based authentication
Object-level authorization
Input validation
Restricted registration fields
Transaction authorization checks
Invalid JWT rejection
Rate limiting
Security headers
8. Test Results Summary
Security Test	Result
BOLA / Object ID Tampering	Protected
Mass Assignment	Protected
Parameter Tampering	Protected
JWT Tampering	Protected
Invalid JWT	Rejected
SQL-Injection-Style Input	Tested
Rate Limiting	Verified
Security Headers	Verified
Burp Suite Interception	Successful
9. Evidence

Testing screenshots are stored in:

screenshots/

The evidence includes:

Home API
Successful registration
Successful JWT login
Profile authentication
BOLA rejection
Mass Assignment testing
Parameter Tampering rejection
Invalid JWT rejection
Rate limiting
Security headers
Burp Suite login interception
Burp Suite password tampering
Burp Suite JWT tampering
Burp Suite object ID tampering
10. Conclusion

The API Security Testing Lab provided practical experience in API development, authentication, authorization, request interception, vulnerability testing, and security remediation.

The project demonstrated how API vulnerabilities can be identified using Postman and Burp Suite and how server-side security controls can reduce unauthorized access and request manipulation.

The testing and remediation process improved the overall security of the locally hosted API application.

This all upto ..... Hosted by api application 

Yes. ✅ Paste the content from # API Security Testing Report all the way through:

The testing and remediation process improved the overall security of the locally hosted API application.

That is the end of the report.