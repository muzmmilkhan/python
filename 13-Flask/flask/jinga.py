from flask import Flask, request, render_template, redirect, url_for

## WSGI application setup
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        return f"Name: {name}, Email: {email}"
    return render_template('form.html')

## Variable Rules
# @app.route('/success/<int:score>')
# def success(score):
#     return f"Form submitted successfully! Your score is: {score}"

## Variable Rules with Conditional Logic
## Jinja2 Template Engine
'''
{{ result }} expression is used to display the result in the template.
{% %} is used for control flow statements like if-else.
{# #} is used for comments.
'''
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "Congratulations! You passed the exam."
    else:
        res = "Sorry, you did not pass the exam."
    return render_template('result.html', result=res, score=score)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = { "result": res, "score": score }
    return render_template('result1.html', result=exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result2.html', result=score)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = request.form.get('science', type=int)
        math = request.form.get('math', type=int)
        datascience = request.form.get('datascience', type=int)
        total_score = (science + math + datascience) / 3
        return redirect(url_for('successres', score=total_score))
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)