# -*- coding: utf-8 -*-

# The imports in this file are order-sensitive

from flask import Flask
from flask.ext.lastuser import Lastuser
from flask.ext.lastuser.sqlalchemy import UserManager
from baseframe import baseframe, assets, Version
import coaster.app

version = Version('0.1.0')

# First, make an app

app = Flask(__name__, instance_relative_config=True)
lastuser = Lastuser()

# Second, import the models and views

import hgapp.models
import hgapp.views
from hgapp.models import db

# Third, setup baseframe and assets

assets['hgapp.js'][version] = 'js/app.js'
assets['hgapp.css'][version] = 'css/app.css'


# Configure the app
def init_for(env):
    coaster.app.init_app(app, env)
    baseframe.init_app(app, requires=['baseframe', 'hgapp'])
    lastuser.init_app(app)
    lastuser.init_usermanager(UserManager(db, hgapp.models.User))
