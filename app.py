from flask import Flask, send_file, request, jsonify
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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

    # Email configuration
    # NOTE: Set these as environment variables in your terminal for security
    SMTP_SERVER = "smtp.gmail.com"  # Use "smtp.office365.com" if sending from an Outlook account
    SMTP_PORT = 587
    SENDER_EMAIL = os.environ.get("EMAIL_USER", "your_sender_email@gmail.com") 
    SENDER_PASSWORD = os.environ.get("EMAIL_PASS", "your_app_password")
    RECEIVER_EMAIL = "dasshuvam305@outlook.com"

    # Construct the email
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = f"Portfolio Contact Form: Message from {name}"
    
    body = f"You have received a new message from your portfolio website.\n\nName: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")
        return jsonify({"status": "error", "message": "Failed to send message. Please try again later."}), 500

    # Respond back to the client
    return jsonify({"status": "success", "message": "Thank you for your message!"})

if __name__ == '__main__':
    # Ensure static directories exist
    os.makedirs('static', exist_ok=True)

    # Run the Flask application
    app.run(debug=True)
