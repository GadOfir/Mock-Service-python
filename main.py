from flask import Flask, jsonify

app = Flask(__name__)

# Mock data
posts = [
    {"id": 1, "title": "Mock Post 1"},
    {"id": 2, "title": "Mock Post 2"}
]

# Endpoint to get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

# Basic endpoint for root URL
@app.route('/', methods=['GET'])
def hello():
    return "Hello, this is a mock API!"

if __name__ == '__main__':
    app.run(port=5000)