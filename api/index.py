from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World", 200

@app.route("/bfhl", methods=["GET"])
def bfhl():
    return jsonify({"operation_code": 1}), 200

@app.post("/bfhl")
def bfhl_post():
    data = request.json.get('data')
    if not isinstance(data, list):
        return jsonify({
            "is_success": False,
            "user_id": "Sujal Vijayvargiya",
            "email": "vijayvargiya_s@srmap.edu.in",
            "roll_number": "AP21110011082",
            "numbers": [],
            "alphabets": [],
            "highest_alphabet": ""
        }), 400

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    highest_alphabet = max(alphabets, key=str.lower) if alphabets else ""

    return jsonify({
        "is_success": True,
        "user_id": "Sujal Vijayvargiya",
        "email": "vijayvargiya_s@srmap.edu.in",
        "roll_number": "AP21110011082",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }), 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404