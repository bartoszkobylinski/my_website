from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import InputRequired, Email, Regexp

class ContactForm(FlaskForm):
    name = StringField(
        "Name", [
        InputRequired("Please enter your name")]
        )
    email = StringField(
        "Email", validators=[
            InputRequired("Please enter your email"), 
            Email()
            ]
            )
    message = TextAreaField(
        "Message", validators=[
            InputRequired("Please enter you message")
            ]
            )
    submit = SubmitField("Send")