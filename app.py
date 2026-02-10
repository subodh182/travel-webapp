# app.py - Simple version (JavaScript ke bina)
from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Firebase setup
try:
    service_account_json = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")
    
    if not service_account_json:
        raise ValueError("FIREBASE_SERVICE_ACCOUNT_JSON environment variable is not set. Please configure it in your .env file or Render dashboard.")
    
    cred = credentials.Certificate(json.loads(service_account_json))
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://travel-webapp-ca17b-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
    print("Firebase initialized successfully")
except Exception as e:
    print(f"Firebase error: {e}")
    raise

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/service')
@app.route('/service.html')
def service():
    return render_template('service.html')

@app.route('/destination')
@app.route('/destination.html')
def destination():
    return render_template('destination.html')

@app.route('/contact')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

# Contact form submit (Python se handle)
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Firebase mein store karo
        contact_ref = db.reference('contacts').push()
        contact_ref.set({
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
            'timestamp': datetime.now().isoformat()
        })
        
        return redirect(url_for('contact'))
    
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode)