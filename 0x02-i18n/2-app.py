#!/usr/bin/env python3
"""
Function that determines best match
with our supported languages
"""


@babel.localeselector
def get_locale():
    """
    Determines best match with our supported
    languages: en, fr
    """
    return request.accept_language.best_match(app.config["LANGUAGES"])

