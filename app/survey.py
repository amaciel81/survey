from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import ContactForm
from os import environ
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.secret_key = environ.get('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Survey(db.Model):
    __table_args__ = {"schema": "survey"}
    name = db.Column(db.String(32), primary_key=True)
    favorite_color = db.Column(db.String(32), nullable=False)
    favorite_pet = db.Column(db.String(8), nullable=False)

    def __init__(self, name, favorite_color, favorite_pet):
        self.name = name
        self.favorite_color = favorite_color
        self.favorite_pet = favorite_pet

    def __repr__(self):
        return '<Name %r>' % self.name


@app.route('/', methods=('GET', 'POST'))
def survey():
    form = ContactForm()

    if request.method == 'POST':
        if not form.validate():
            message = 'Please fill in all fields'
        else:
            try:
                preferences = Survey(form.name.data, form.favorite_color.data, form.favorite_pet.data)
                db.session.add(preferences)
                db.session.commit()
                message = 'Information successfully saved!'
            except IntegrityError:
                message = 'Error: name "{name}" is already in the database'.format(name=form.name.data)
            except Exception as err:
                message = "Unknown error: {error}".format(error=str(err))

        return render_template('result.html', message=message)

    elif request.method == 'GET':
        return render_template('survey.html', form=form)


if __name__ == '__main__':
    app.run()
