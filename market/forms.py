from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[
                           Length(min=5), DataRequired()])
    email_address = StringField(label="Email address", validators=[
                                Email(), DataRequired()])
    password1 = PasswordField(label="Password", validators=[
                              Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password",
                              validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label="Create Account")
