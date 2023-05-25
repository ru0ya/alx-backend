#!/usr/bin/env python3
"""
Instantiates the Babel object
"""


from flask import Flask, render_template
from flask_babel import Babel

# Setting up flask app
app = Flask(__name__)

# Instantiates Babel in app
babel = Babel(app)


class Config(object):
    """
    Configures available languages in the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello():
    """
    Returns: Html template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
