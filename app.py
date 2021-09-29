"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html'), 200
    else:
        return page_not_found


@app.route('/about')
def about():
    if request.method == 'GET':
        return render_template('about.html')
    else:
        return page_not_found


@app.route('/page_not_found')
def page_not_found():
    bad_response = requests.get()
    if request.method == 'GET' and bad_response.status_code != 200:
        return render_template('bad_request.html')