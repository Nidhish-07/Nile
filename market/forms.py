from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username=StringField(label="Username")
    email_address=StringField(label="Email address")
    password1=PasswordField(label="Password")
    password2=PasswordField(label="Confirm Password")
    submit=SubmitField(label="Create Account")
