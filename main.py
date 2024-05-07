from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load user data from external JSON file
with open('users.json', 'r') as file:
    users = json.load(file)

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint to get user's name and birthday by ID
@app.route('/users/birthday/<int:user_id>', methods=['GET'])
def get_user_birthday(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify({"name": user["name"], "birthdate": user["birthdate"]})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)