from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import SubmitField, HiddenField, StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email

class Form(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

class GeminiForm(FlaskForm):
    prompt = TextAreaField('Question', validators=[DataRequired()])
    submit = SubmitField('Get answer')
=======
from wtforms import SubmitField, StringField, IntegerField, SelectField, HiddenField
from wtforms.validators import DataRequired, NumberRange

class Form(FlaskForm):
    occasion = SelectField(
        'Occasion',
        choices=[('breakup', 'Break Up'), ('quit', 'Quit Job'), ('other', 'Other')],
        validators=[DataRequired()]
    )
    name = StringField('Name', validators=[DataRequired()])
    details = StringField('Details (e.g., "He never listens")', validators=[DataRequired()])
    rudeness = IntegerField('Rudeness Level (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Generate Script')

class DownloadForm(FlaskForm):
    download = HiddenField('Download Audio')
>>>>>>> e529a8a495c5f833b40fb4a080d9827df0c3a226
