#!/usr/bin/env python3
"""
Functon to parameterize templates using
'_' or 'gettext'
"""


from flask import flash
from flask-babel import gettext


def parameterize_templates(home_title, home_header):
    flash(gettext('%(title)s', title=home_title))
    flash(gettext('%(h1)s', h1=home_header))
