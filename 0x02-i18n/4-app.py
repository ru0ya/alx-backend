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
    locale.setlocale(locale.LC_ALL, 'fr')

    locale = request.args.get('locale')

    if locale and locale in LANGUAGES:
        return f"{locale}"
    else:
        return request.accept_language.best_match(app.config["LANGUAGES"])
