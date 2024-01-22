from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

user = [
    {'name': 'Fernando', 'senha':12345678}
    ]

@app.route('/', methods=['GET'])
def home():
    return jsonify(user)

@app.route('/', methods=['POST'])
def add_user():
    user.append(request.get_json())
    return 'success', 204

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)