from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Set the path for static files like images and CSS
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    # Fetch data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # For now, print the form data to the console
    print(f"Name: {name}, Email: {email}, Message: {message}")

    # Return a JSON response
    return jsonify({
        'status': 'success',
        'message': 'Thank you for contacting me!'
    })

if __name__ == '__main__':
    # Ensure templates folder exists
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # Ensure static folder exists
    if not os.path.exists('static'):
        os.makedirs('static')

    app.run(debug=True)
