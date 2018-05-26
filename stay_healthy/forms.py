# app/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

# from ..models import Employee

class ContactForm(FlaskForm):
    """
    Form for users to create new account
    """
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail address', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    # last_name = StringField('Last Name', validators=[DataRequired()])
    # password = PasswordField('Password', validators=[
    #                                     DataRequired(),
    #                                     EqualTo('confirm_password')
    #                                     ])
    # confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Submit')

    # def validate_email(self, field):
    #     if Employee.query.filter_by(email=field.data).first():
    #         raise ValidationError('Email is already in use.')

    # def validate_username(self, field):
    #     if Employee.query.filter_by(username=field.data).first():
    #         raise ValidationError('Username is already in use.')

# class LoginForm(FlaskForm):
#     """
#     Form for users to login
#     """
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Login')