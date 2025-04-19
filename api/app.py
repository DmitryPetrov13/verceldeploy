from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('../static', 'index.html')

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Flask on Vercel!"})

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

# Vercel requires this to be named 'app'
app = app
