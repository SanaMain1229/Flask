from flask import Flask, render_template, request, redirect, make_response, session, url_for
app = Flask(__name__)
app.secret_key = 'testing_only'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f'Logged in as {username} <br> ' + \
        "<br><b><a href ='/logout'>click here to logout</a></b>"
    
    return "Your are not logged in <br><a href='/login'><b>" + \
            "Click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)