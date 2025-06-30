from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

# Example: Hashing a password
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

# Example: Checking a password
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

# Route to hash a password
@app.route('/hash', methods=['POST'])
def hash_route():
    data = request.json
    password = data.get("password")
    if not password:
        return jsonify({"error": "Password required"}), 400
    hashed = hash_password(password)
    return jsonify({"hashed_password": hashed})

# Route to verify a password
@app.route('/verify', methods=['POST'])
def verify_route():
    data = request.json
    password = data.get("password")
    hashed = data.get("hashed_password")
    if not password or not hashed:
        return jsonify({"error": "Password and hash required"}), 400
    is_valid = check_password(password, hashed)
    return jsonify({"valid": is_valid})

if __name__ == '__main__':
    app.run(debug=True)
