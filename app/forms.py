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
from wtforms.widgets.core import RangeInput

from wtforms.validators import ValidationError

def not_empty_choice(form, field):
    if not field.data or field.data.strip() == '':
        raise ValidationError(f"Please select the {field.label.text.lower()}")


class Form(FlaskForm):
    occasion = SelectField(
    'Occasion',
    choices=[
        ('', '--Please Select Occasion--'),
        ('breakup', 'Break Up'),
        ('quit', 'Quit Job'),
        ('other', 'Other')
    ],
    default='',
    validators=[not_empty_choice])

    name = StringField('Name', validators=[DataRequired()])
    language = SelectField('Language', choices=[('','--Please Select An Output Language--'),('English','English'),
                                                ('French','French'),('Japanese','Japanese'),('Spanish','Spanish')],
                           default='',
                           validators=[not_empty_choice])
    details = StringField('Details', validators=[DataRequired()])
    rudeness = IntegerField("Rudeness", widget=RangeInput(), default=5)
    submit = SubmitField('Generate Script')

class DownloadForm(FlaskForm):
    download = HiddenField('Download Audio')
>>>>>>> e529a8a495c5f833b40fb4a080d9827df0c3a226
