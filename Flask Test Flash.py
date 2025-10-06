from flask import Flask, render_template, redirect, url_for, make_response, flash, request

app = Flask(__name__)
app.secret_key = 'RandomAll'

@app.route('/')
def index():
    return render_template('index_flash.html')

@app.route('/login_flash', methods = ['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Username or password, try again!'
        else:
            flash ('You were successfully logged in')
            return redirect(url_for('index'))
    
    return render_template('login_flash.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)
