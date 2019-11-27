from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired("Please enter your name")])
    email = StringField("Email", validators=[InputRequired("Please enter your mail")])
    message = TextAreaField("Message", validators=[InputRequired("Please enter you message")])
    submit = SubmitField("Send")