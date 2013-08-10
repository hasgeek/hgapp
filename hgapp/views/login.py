# -*- coding: utf-8 -*-

from flask import redirect, flash, Markup, escape
from coaster.views import get_next_url
from baseframe import _
from baseframe.forms import render_message

from .. import app, lastuser
from ..models import db


@app.route('/login')
@lastuser.login_handler
def login():
    return {'scope': 'id'}


@app.route('/logout')
@lastuser.logout_handler
def logout():
    flash(u"You are now logged out", category='success')
    return get_next_url()


@app.route('/login/redirect')
@lastuser.auth_handler
def lastuserauth():
    return redirect(get_next_url())


@app.route('/login/notify', methods=['POST'])
@lastuser.notification_handler
def lastusernotify(user):
    # Perform operations here if required.
    # Warning: this *could* be a spoof call, so ignore all request data.
    # Only trust the 'user' parameter to this function.
    db.session.commit()


@lastuser.auth_error_handler
def lastuser_error(error, error_description=None, error_uri=None):
    if error == 'access_denied':
        flash("You denied the request to login", category='error')
        return redirect(get_next_url())
    return render_message(
        title="Error: {0}".format(error),
        message=Markup(
            "<p>{desc}</p><p>URI: {uri}</p>".format(
                desc=escape(error_description or ''), uri=escape(error_uri or _('NA')))
            )
        )
