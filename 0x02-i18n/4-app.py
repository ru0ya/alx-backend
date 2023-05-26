#!/usr/bin/env python3
"""
Function that determines best match
with our supported languages
"""
from flask import Flask, render_template, request, flash
from flask_babel import Babel
import locale


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configures available languages in the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determines best match with our supported
    languages: en, fr
    """
    locale.setlocale(locale.LC_ALL, 'fr')

    locale = request.args.get('locale')

    if locale and locale in app.config["LANGUAGES"]:
        return locale
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def root():
    """
    Returns: Html template
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
