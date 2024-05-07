from flask import Flask, jsonify

app = Flask(__name__)

# Mock data with different data types
users = [
    {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "birthdate": "1990-05-15"
    },
    {
        "id": 2,
        "name": "Bob",
        "email": "bob@example.com",
        "birthdate": "1985-10-20"
    }
]

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