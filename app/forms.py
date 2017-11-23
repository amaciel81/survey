from flask_wtf import Form
from wtforms import StringField, SelectField, SubmitField, validators


class ContactForm(Form):
    name = StringField('Name:', [validators.DataRequired()])
    favorite_color = StringField('Favorite color:', [validators.DataRequired()])
    favorite_pet = SelectField('Favorite pet:', choices=[('cat', 'Cat'), ('dog', 'Dog')])
    submit = SubmitField('Submit')
