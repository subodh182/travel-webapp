# app.py - Simple version (JavaScript ke bina)
from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

app = Flask(__name__)

# Firebase setup
try:
    cred = credentials.Certificate('firebase-serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://travel-webapp-ca17b-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
except Exception as e:
    print(f"Firebase error: {e}")

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
    app.run(debug=True)