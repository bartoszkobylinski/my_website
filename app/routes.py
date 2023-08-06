import json.decoder
import logging
import os
import requests
from flask import Flask, flash, render_template, session, request, url_for, redirect

app = Flask(__name__)

logging.basicConfig(filename="my_website_logs.log", level=logging.WARNING)

app.secret_key = os.getenv("MY_WEBSITE_FLASK_SESSION_SECRET_KEY")
milamber_webhook = os.getenv("MILAMBER_WEBHOOK")


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


@app.route('/milamber')
def milamber():
    conversation = session.get("conversation", [])
    if not conversation:
        try:
            greeting_message_json = {
                "query": "Greet kindly a user and tell in a short way who you are with telling your name and who do you"
                         "assist?",
                "type": "query"
            }
            response = requests.post(milamber_webhook, json=greeting_message_json)
            greeting_response = response.json()
            conversation.append(('milamber', greeting_response.get('answer', '')))
        except json.decoder.JSONDecodeError:
            flash("'Something went wrong with the server. Please try again later.")
        session['conversation'] = conversation
    return render_template('milamber.html', title="Milamber", conversation=conversation)


@app.route('/ask_milamber', methods=['POST'])
def ask_milamber():
    user_message = request.form['user_message']
    user_message_json = {
        "query": user_message,
        "type": "query"
    }
    try:
        response = requests.post(milamber_webhook, json=user_message_json)
        milamber_response = response.json()

        conversation = session.get('conversation', [])
        conversation.append(('user', user_message))
        conversation.append(('milamber', milamber_response.get('answer', '')))
        session['conversation'] = conversation
    except json.decoder.JSONDecodeError:
        flash('Something went wrong with the server. Please try again later.')

    return redirect(url_for('milamber'))
