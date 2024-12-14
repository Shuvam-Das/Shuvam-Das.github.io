from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    # Fetch form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Log the form data (this could be saved to a database or sent via email in a real app)
    print(f"Contact Form Submission: Name={name}, Email={email}, Message={message}")

    # Respond back to the client
    return jsonify({"status": "success", "message": "Thank you for reaching out! Your message has been received."})

if __name__ == '__main__':
    # Ensure required directories exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    if not os.path.exists('static'):
        os.makedirs('static')

    app.run(debug=True)
