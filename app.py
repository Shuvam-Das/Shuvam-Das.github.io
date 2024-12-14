from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(f"Received: Name={name}, Email={email}, Message={message}")
    return jsonify({"status": "success", "message": "Message received!"})

if __name__ == '__main__':
    # Ensure required directories exist
    if not os.path.exists('index.html'):
        os.makedirs('index.html')
    if not os.path.exists('static'):
        os.makedirs('static')

    app.run(debug=True)