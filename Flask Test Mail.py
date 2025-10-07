from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'm*******'
app.config['MAIL_PASSWORD'] = '******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', sender = 'input sender here', recipients=['must be a list, input sender here'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app.run(debug=True)

#to access gmail go here https://myaccount.google.com/security , then turn on 2 step, verification
