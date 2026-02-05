from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)