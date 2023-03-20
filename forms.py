from wtforms import StringField, EmailField, PasswordField,SubmitField,HiddenField, BooleanField
from wtforms.validators import InputRequired, DataRequired, Email,EqualTo,Length,Regexp
from flask_wtf import FlaskForm



class RegistrationForm(FlaskForm):
    fullname = StringField("Name", validators=[DataRequired(), Length(min=10, max=70,message="Name should have atleast 10 characters")])
    Email = EmailField('Email',validators=[DataRequired(),Email(message='Please enter your email')])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8, max=12)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password',message="Password MUST match")])
    submit = SubmitField('Register')
    
    
class LoginForm(FlaskForm):
    Email = EmailField('Email',validators=[InputRequired(),Email('Enter the correct email')])
    password = PasswordField('Password',validators=[InputRequired(),Length(min=8, max=20)])
    remember = BooleanField('Remember me')