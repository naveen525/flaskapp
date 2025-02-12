from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

class GreetingForm(FlaskForm):
    """A form that asks for a user's name."""
    name = StringField('Name', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def home():
    form = GreetingForm()
    if form.validate_on_submit():
        name = form.name.data
        return render_template('greeting.html', name=name)
    return render_template("index.html",form = form)

@app.route("/about")
def about():
    return render_template('about.html', name='Naveen', fact ='I am a Flask developer')

if __name__ == "__main__":
    app.run(debug=True)