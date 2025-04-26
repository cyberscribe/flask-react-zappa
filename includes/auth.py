from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

# Placeholder login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # TODO: Implement real authentication logic (hash checking etc.)
    if username == "admin" and password == "password":
        return jsonify({"message": "Login successful", "token": "fake-jwt-token"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Placeholder logout route
@auth_bp.route('/logout', methods=['POST'])
def logout():
    # TODO: Implement real session clearing logic
    return jsonify({"message": "Logged out"}), 200
