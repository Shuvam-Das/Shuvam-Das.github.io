from flask import Flask, send_file, request, jsonify
import os

# Set up Flask app
app = Flask(__name__)

@app.route('/')
def index():
    # Directly serve index.html from the current directory
    return send_file('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    # Fetch form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Log the form data
    print(f"Contact Form Submission: Name={name}, Email={email}, Message={message}")

    # Respond back to the client
    return jsonify({"status": "success", "message": "Thank you for your message!"})

if __name__ == '__main__':
    # Ensure static directories exist
    os.makedirs('static', exist_ok=True)

    # Run the Flask application
    app.run(debug=True)
