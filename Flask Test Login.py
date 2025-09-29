from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success_post/<name>')
def success_post(name):
    return f'welcome post {name}'

@app.route('/success_get/<name>')
def success_get(name):
    return f'welcome get {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success_post', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success_get', name = user))

if __name__ == '__main__':
    app.run(debug=True)