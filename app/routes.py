import logging
from flask import Flask, render_template


app = Flask(__name__)

logging.basicConfig(filename="my_website_logs.log", level=logging.WARNING)


@app.route('/')
def main():
    return render_template("main.html", title="Main Page")


@app.route('/index')
def index():
    return render_template("index.html", title='Index Page')


@app.route('/about_me')
def about_me():
    return render_template('about_me.html', title='About me')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='My projects')


@app.route('/thanks')
def thanks():
    return render_template('thanks.html', title='Thank you')
