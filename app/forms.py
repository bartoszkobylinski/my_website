from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired

class ContactForm(Form):
    name = TextField("Name", validators=[DataRequired("Please enter your name")])
    email = TextField("Email", validators=[DataRequired("Please enter your mail")])
    message = TextAreaField("Message", validators=[DataRequired("Didn't you want to say something?")])
    submit = SubmitField("Send")