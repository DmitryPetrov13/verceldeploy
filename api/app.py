from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('../static', 'index.html')

@app.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask on Vercel!'}

@app.route('/api/greet/<name>')
def greet(name):
    return {'message': f'Hello, {name}!'}
