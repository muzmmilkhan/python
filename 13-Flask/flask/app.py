from flask import Flask

### WSGI Application
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!, Welcome to Flask!"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Application!, Enjoy your stay!"

if __name__ == '__main__':
    app.run(debug=True)