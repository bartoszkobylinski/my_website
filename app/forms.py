from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import InputRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField(
        "Name *", [
            InputRequired("Please enter your name"),
            Length(min=1,
                   max=35,
                   message="You can provide name with max 35 characters")]
                        )
    email = StringField(
        "Email *", validators=[
            InputRequired("Please enter your email"),
            Email()
            ]
            )
    message = TextAreaField(
        "Message *", validators=[
            InputRequired("Please enter you message"),
            Length(min=1,
                   max=200,
                   message="Message can contain only 200 characters")
            ]
            )
    question = StringField("Please enter a result of 15 + 16 *",
                           validators=[
                                InputRequired(
                                    "Please enter a result of 15+16"),
                                Length(min=1, max=2)
                                         ])
    submit = SubmitField("Send")
