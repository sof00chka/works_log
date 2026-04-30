from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class DepartmentsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    chief = StringField('Chief')
    members = StringField('Members')
    email = StringField('Email')
    submit = SubmitField('Добавить')