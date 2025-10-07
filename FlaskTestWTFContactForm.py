from flask_wtf import FlaskForm
from wtforms import *
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
    name = StringField("Name of Student", [validators.DataRequired("Please enter your name.")])
    gender = RadioField('Gender', choices =['M', 'Male', 'F', 'Female'])
    address = TextAreaField("Address")
    email =  StringField("Email", [validators.DataRequired("Please Enter your email address")])
    age = IntegerField("Age")
    language = SelectField('Languages', choices=[('cpp', 'c++'), ('py', 'python')])
    submit = SubmitField("Send")