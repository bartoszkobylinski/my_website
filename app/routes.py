from app import app
from flask import render_template, flash, request, redirect
from app.forms import ContactForm


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/contact', methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST' and form.validate():
        return render_template("thanks.html")
    elif request.method == 'GET':
        return render_template("contact.html", form=form)

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')
    
@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')