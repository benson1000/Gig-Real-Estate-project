from wtforms import StringField, EmailField, PasswordField,SubmitField,HiddenField, BooleanField
from wtforms.validators import InputRequired, DataRequired, Email,EqualTo,Length,Regexp
from flask_wtf import FlaskForm



class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=4, max=15)])
    email = EmailField('email',validators=[DataRequired(),Email(message='Please enter your email')])
    password = PasswordField('Password',validators=[InputRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo(password)])
    Register = SubmitField('Register')
    
    
class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[InputRequired(),Email('Enter the correct email')])
    password = PasswordField('Password',validators=[InputRequired(),Length(min=4, max=20)])
    remember = BooleanField('Remember me')