from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "temperature": 27.5,
        "fanStatus": "OFF"
    })

@app.route('/temperature', methods=['GET'])
def get_temperature():
    return jsonify({
        "temperature": 27.5
    })

@app.route('/fan-status', methods=['GET'])
def get_fan_status():
    return jsonify({
        "fanStatus": "OFF"
    })

@app.route('/login', methods=['POST'])
def login():
    return jsonify({
        "success": True,
        "message": "Login successful"
    })

@app.route('/signup', methods=['POST'])
def signup():
    return jsonify({
        "success": True,
        "message": "User registered successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)
