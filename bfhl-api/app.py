from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1})

@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    data = request.json.get('data', [])
    if not isinstance(data, list):
        return jsonify({
            "is_success": False,
            "user_id": "your_fullname_dob",
            "email": "your_email@xyz.com",
            "roll_number": "ABCD123",
            "numbers": [],
            "alphabets": [],
            "highest_alphabet": []
        }), 400

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    return jsonify({
        "is_success": True,
        "user_id": "your_fullname_dob",
        "email": "your_email@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": sorted(alphabets, reverse=True)[0] if alphabets else None
    })

if __name__ == '__main__':
    app.run()