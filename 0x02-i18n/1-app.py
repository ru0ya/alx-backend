#!/usr/bin/env python3
"""
Instantiates the Babel object 
"""


from flask import Flask, render_template
from flask-babel import Babel

# Setting up flask app
app = Flask(__name__)

#Instantiates Babel in app
babel = Babel(app)

class Config(object):
    """
    Configures available languages in the app
    """
    LANGUAGES = ["en", "fr"]


app.config["DEFAULT_LOCALE"] = "en"
app.config["DEFAULT_TIMEZONE"] = "UTC"
