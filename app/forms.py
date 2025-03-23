from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField, StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email

class Form(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

class GeminiForm(FlaskForm):
    prompt = TextAreaField('Question', validators=[DataRequired()])
    submit = SubmitField('Get answer')