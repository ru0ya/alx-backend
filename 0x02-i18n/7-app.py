#!/usr/bin/env python3
"""
Function that determines best match
with our supported languages
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import locale
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


@app.route('/')
def root():
    """
    Returns: Html template
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    Determines best match with our supported
    languages: en, fr
    """
    locale = request.args.get('locale', None)

    if locale and locale in app.config['LANGUAGES']:
        return f"{locale}"

    locale = request.headers.get('locale', None)

    if locale and locale in app.config['LANGUAGES']:
        return f"{locale}"

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    Returns a user dictionary or None if ID cannot
    be found or if login_as was not passed
    """
    user_id = request.args.get('login_as')

    if user_id and int(user_id) in users:
        return users[int(user_id)]

    return None


@app.before_request
def before_request():
    """
    Uses get_user to find a user if any
    and set is as global
    """
    current_user = get_user()
    g.user = current_user


@babel.timezoneselector
def get_timezone():
    user_timezone = request.args.get('timezone')

    if user_timezone in pytz.all_timezones:
        return user_timezone
    else:
        raise pytz.exception.UnknownTimeZoneError

    userId = request.args.get('login_as')
    user_timezone = users[int(userId)]['timezone']

    if user_timezone in pytz.all_timezones:
        return user_timezone
    else:
        raise pytz.exception.UnknownTimeZoneError


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
