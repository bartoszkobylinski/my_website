from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, ValidationError, StringField
from wtforms.validators import InputRequired

class ContactForm(Form):
    name = StringField("Name", validators=[InputRequired("Please enter your name")])
    email = StringField("Email", validators=[InputRequired("Please enter your mail")])
    message = TextAreaField("Message", validators=[InputRequired("Didn't you want to say something?")])
    submit = SubmitField("Send")