from flask import Flask, render_template, request

## WSGI application setup
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        return f"Hello, {name}!"
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)