from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder='../public')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Flask API!"})

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

# Vercel requires this handler
def handler(event, context):
    return app(event, context)
