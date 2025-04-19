from http.server import BaseHTTPRequestHandler
from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='../public')

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Vercel Flask!"})

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

# Vercel serverless function handler
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Serverless function running", "utf-8"))

# Required for Vercel
def handler(request):
    return app(request.environ, request.start_response)
