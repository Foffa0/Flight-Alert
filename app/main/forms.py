from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AirportForm(FlaskForm):
    query = StringField('Airport', validators=[DataRequired()])
    submit = SubmitField('Speichern')