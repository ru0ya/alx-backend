#!/usr/bin/env python3
"""
Function that determines best match
with our supported languages
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
import locale


app = Flask(__name__)
# instantiate babel object
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
def root() -> str:
    """
    Returns: Html template
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Determines best match with our supported
    languages: en, fr
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run()
