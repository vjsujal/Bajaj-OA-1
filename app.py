from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index_get():
    return "<h1>Welcome to the API</h1>"

@app.get('/bfhl')
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

@app.post("/bfsl")
def predict():
    data = request.json.get('data')
    if not isinstance(data, list):
        return jsonify({
            "is_success": False,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": [],
            "alphabets": [],
            "highest_alphabet": []
        }), 400

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

    return jsonify({
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }), 200
