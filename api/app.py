from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/hello')
def hello():
    return jsonify({
        "message": "Hello from the API!",
        "status": "success"
    })

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({
        "message": f"Hello, {name}!",
        "status": "success"
    })
