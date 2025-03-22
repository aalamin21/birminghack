from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email
from flask_login import current_user
from app import db

class Form(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')