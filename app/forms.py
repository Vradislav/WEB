from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired()])
    last_name = StringField(label='Last name', validators=[DataRequired()])
    position = StringField(label='Position', validators=[DataRequired()])
    submit = SubmitField(label='Add user')
