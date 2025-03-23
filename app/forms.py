from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, HiddenField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.core import RangeInput

from wtforms.validators import ValidationError

def not_empty_choice(form, field):
    if not field.data or field.data.strip() == '':
        raise ValidationError("Please select an occasion.")


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
    details = StringField('Details', validators=[DataRequired()])
    rudeness = IntegerField("Rudeness", widget=RangeInput(), default=5)
    submit = SubmitField('Generate Script')

class DownloadForm(FlaskForm):
    download = HiddenField('Download Audio')