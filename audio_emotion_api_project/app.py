
from flask import Flask, request, jsonify
from model import predict_emotion

app = Flask(__name__)

@app.route('/api/emotion', methods=['POST'])
def emotion():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    result = predict_emotion(file)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
