from flaskblog.models import User
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email,EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    user_name = StringField('Username', validators = [DataRequired(), Length(min =2, max = 20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_user_name(self, user_name):
        user = User.query.filter_by(user_name=user_name.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')
