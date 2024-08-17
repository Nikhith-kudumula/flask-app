from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify(greeting=f"Hello, {name}!")

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    result = data['a'] + data['b']
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

