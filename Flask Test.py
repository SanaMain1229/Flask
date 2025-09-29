# Importing the Flask module
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

#app name
app = Flask(__name__)
#app.config['SECRET KEY'] = '207-015-068'
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

#toolbar = DebugToolbarExtension(app)

#route section
@app.route("/hello")
def hello_world():
    return 'Hello World'

#setting the name
@app.route("/hello/<name>")
def hello_name(name):
    return f'Hello {name}!' 

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return f'Blog Number {postID}'

app.route('/rev/<float:revNo>')
def revision(revNo):
    return f'Revision Number {revNo}'

#adding url route commands, to call a function use lambda
app.add_url_rule("/", "hello", hello_name)

if __name__ == '__main__':
    #app run can consist of
    #app.run(host, port, debug, options)
    app.run()
    