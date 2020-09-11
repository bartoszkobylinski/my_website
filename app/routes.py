from app import app
from flask import render_template, request
from app.forms import ContactForm
from flask_mail import Mail, Message
from app.credentials import credentials

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_DEFAULT_SENDER"] = credentials.get('username')
app.config["MAIL_USERNAME"] = credentials.get('username')
app.config["MAIL_PASSWORD"] = credentials.get('password')

mail = Mail()

mail.init_app(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Main Page')


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
            mail.send(message)
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
