from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField
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
