# -*- coding: utf-8 -*-

# The imports in this file are order-sensitive

from flask import Flask
from flask.ext.assets import Environment, Bundle
from flask.ext.lastuser import LastUser
from baseframe import baseframe, baseframe_js, baseframe_css
import coaster.app

# First, make an app

app = Flask(__name__, instance_relative_config=True)
lastuser = LastUser()

# Second, after config, import the models and views

import hgapp.models
import hgapp.views

# Third, setup baseframe and assets

app.register_blueprint(baseframe)

assets = Environment(app)
js = Bundle(baseframe_js)
css = Bundle(baseframe_css,
             'css/app.css')

# Configure the app
def init_for(env):
    coaster.app.init_app(app, env)
    assets.register('js_all', js)
    assets.register('css_all', css)
    lastuser.init_app(app)
