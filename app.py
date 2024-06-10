from flask import Flask, request, jsonify  # Added jsonify import

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    # Process the data here
    response = {"message": "Data received", "data": data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
