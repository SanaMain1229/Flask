from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello_score/<int:score>')
def hello_score(score):
    return render_template('hello.html', marks = score)

@app.route('/hello_name/<user>')
def hello_name(user):
    return render_template('hello.html', name = user, marks = 51)

@app.route('/result')
def result():
    dict = {'phy':50, 'che':60, 'maths':70}
    return render_template('result.html', result = dict)

if __name__ == '__main__':
    app.run(debug=True)