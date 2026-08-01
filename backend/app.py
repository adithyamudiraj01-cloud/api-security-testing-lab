from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import Flask, request
from flask_cors import CORS
import json
import os
import jwt
import datetime

app = Flask(__name__)
cors = CORS(app)
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
        default_limits=[]
)
secret_key = "mysecretkey123"  

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(BASE_DIR, "users.json")
print(f"Reading file from: {os.path.abspath(USER_FILE)}")
# Create users.json automatically if it doesn't exist
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as file:
        json.dump([], file)

# ---------------- HOME API ----------------
@app.route("/")
def home():
    return {
        "message": "Welcome to API Security Testing Lab",
        "status": "success"
    }

# ---------------- REGISTER API ----------------
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    # Check if data exists
    if not data:
        return {
            "message": "No data received"
        }, 400

    # Validate required fields
    required_fields = ["username", "email", "password"]

    for field in required_fields:
        if field not in data or data[field] == "":
            return {
                "message": f"{field} is required"
            }, 400

    # Read users
    with open(USER_FILE, "r") as file:
        users = json.load(file)

    # Check duplicate email
    for user in users:
        if user["email"] == data["email"]:
            return {
                "message": "Email already exists"
            }, 409

        new_user = {
    "id": len(users) + 1,
    "username": data["username"],
    "email": data["email"],
    "password": data["password"]
}

    users.append(new_user)

    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

    return {
        "message": "Registration Successful",
        "user": new_user
    }, 201
# ---------------- LOGIN API ----------------
@app.route("/login", methods=["POST"])
@limiter.limit("5 per minute")  # Limit to 5 requests per minute
def login():

    print("Login API called")

    data = request.get_json()
    print("Received data:", data)

    if not data:
        return {"message": "No data received"}, 400

    with open(USER_FILE, "r") as file:
        users = json.load(file)

    print("Users loaded:", users)

    for user in users:
        if user["email"] == data["email"] and user["password"] == data["password"]:

            print("User found")

            token = jwt.encode(
                {
                    "user_id": user["id"],
                    "username": user["username"],
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                },
                secret_key,
                algorithm="HS256"
            )

            print("Token generated")

            return {
                "message": "Login Successful",
                "token": token
            }, 200

    return {
        "message": "Invalid Email or Password"
    }, 401
## ---------------- PROFILE API ----------------
@app.route("/profile", methods=["GET"])
def profile():

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return {
            "message": "Token is missing"
        }, 401

    try:
        token = auth_header.split(" ")[1]

        jwt.decode(
            token,
            secret_key,
            algorithms=["HS256"]
        )

    except Exception:
        return {
            "message": "Invalid or Expired Token"
        }, 401

    with open(USER_FILE, "r") as file:
        users = json.load(file)

    return {
        "total_users": len(users),
        "users": users
    }
# ---------------- GET USER API ----------------
@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):

    logged_in_user = 1

    if user_id != logged_in_user:
        return {
            "message": "Forbidden"
        }, 403

    with open(USER_FILE, "r") as file:
        users = json.load(file)

    for user in users:
        if user["id"] == user_id:
            return user

    return {
        "message": "User not found"
    }, 404
    # ---------------- SEARCH API ----------------
@app.route("/search", methods=["POST"])
def search():

    data = request.get_json()

    if not data or "username" not in data:
        return {
            "message": "Username is required"
        }, 400

    username = data["username"]

    with open(USER_FILE, "r") as file:
        users = json.load(file)

    results = []

    for user in users:
        if username.lower() in user["username"].lower():
            results.append(user)

    return {
        "results": results
    }
    # ---------------- UPDATE USER API ----------------
@app.route("/update", methods=["POST"])
def update_user():

    data = request.get_json()

    if not data or "id" not in data or "username" not in data:
        return {
            "message": "id and username are required"
        }, 400

    with open(USER_FILE, "r") as file:
        users = json.load(file)

    for user in users:
        if user["id"] == data["id"]:
            user["username"] = data["username"]

            with open(USER_FILE, "w") as file:
                json.dump(users, file, indent=4)

            return {
                "message": "User Updated",
                "user": user
            }

    return {
        "message": "User not found"
    }, 404
    # ---------------- SECURITY HEADERS ----------------
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response
    # ---------------- TRANSFER API ----------------
@app.route("/transfer", methods=["POST"])
def transfer():

    data = request.get_json()

    if not data:
        return {"message": "No data received"}, 400

    required_fields = ["from_account", "to_account", "amount"]

    for field in required_fields:
        if field not in data:
            return {"message": f"{field} is required"}, 400

    # Simulated logged-in user's account
    logged_in_account = "1001"

    # Authorization check
    if data["from_account"] != logged_in_account:
        return {
            "message": "Forbidden: You cannot transfer from this account"
        }, 403

    # Basic amount validation
    if not isinstance(data["amount"], (int, float)) or data["amount"] <= 0:
        return {
            "message": "Invalid amount"
        }, 400

    return {
        "from_account": data["from_account"],
        "to_account": data["to_account"],
        "amount": data["amount"],
        "message": "Transfer Successful"
    }, 200
# ---------------- SECURE ACCOUNT API ----------------
@app.route("/account/<int:user_id>", methods=["GET"])
def account(user_id):

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        return {
            "message": "Token is missing"
        }, 401

    try:
        token = auth_header.split(" ")[1]

        decoded = jwt.decode(
            token,
            secret_key,
            algorithms=["HS256"]
        )

        logged_in_user = decoded["user_id"]

    except Exception:
        return {
            "message": "Invalid or Expired Token"
        }, 401

    if user_id != logged_in_user:
        return {
            "message": "Forbidden"
        }, 403

    with open(USER_FILE, "r") as file:
        users = json.load(file)

    for user in users:
        if user["id"] == user_id:
            return {
                "id": user["id"],
                "username": user["username"],
                "email": user["email"]
            }, 200

    return {
        "message": "User not found"
    }, 404
if __name__ == "__main__":
    app.run(debug=True)