import logging
from flask import Flask, render_template, request
from app.forms import ContactForm
from flask_mail import Mail, Message
from app.credentials import credentials

app = Flask(__name__)

logging.basicConfig(filename="my_website_logs.log", level=logging.WARNING)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_DEFAULT_SENDER"] = credentials.get('username')
app.config["MAIL_USERNAME"] = credentials.get('username')
app.config["MAIL_PASSWORD"] = credentials.get('password')

mail = Mail()

mail.init_app(app)


@app.route('/')
def main():
    return render_template("main.html", title="Main Page")


@app.route('/index')
def index():
    return render_template("index.html", title='Index Page')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    question = "Oslo"
    if request.method == 'POST' and form.validate():
        message = Message(
            subject="New message has been sent through your website",
            recipients=[credentials.get('username')])
        message.body = f"""From:{form.name.data} and from email
                        {form.email.data} and message {form.message.data}."""
        if form.question.data == question:
            try:
                mail.send(message)
                logging.info("Email sent successfully")
            except Exception as error:
                logging.error(f"Error occurred while sending email: {error}")
        return render_template("thanks.html")
    else:
        return render_template("contact.html", title='Contact Page', form=form)


@app.route('/about_me')
def about_me():
    return render_template('about_me.html', title='About me')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='My projects')


@app.route('/thanks')
def thanks():
    return render_template('thanks.html', title='Thank you')
