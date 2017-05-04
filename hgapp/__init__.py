# -*- coding: utf-8 -*-

# The imports in this file are order-sensitive

from __future__ import absolute_import
from flask import Flask
from flask_migrate import Migrate
from flask_lastuser import Lastuser
from flask_lastuser.sqlalchemy import UserManager
from baseframe import baseframe, assets, Version
import coaster.app
from ._version import __version__

version = Version(__version__)

# First, make an app

app = Flask(__name__, instance_relative_config=True)
lastuser = Lastuser()

# Second, import the models and views

from . import models, views  # NOQA
from .models import db

# Third, setup baseframe and assets

assets['hgapp.js'][version] = 'js/app.js'
assets['hgapp.css'][version] = 'css/app.css'

# Configure the app
coaster.app.init_app(app)
db.init_app(app)
db.app = app
migrate = Migrate(app, db)
baseframe.init_app(app, requires=['baseframe-bs3', 'hgapp'])
lastuser.init_app(app)
lastuser.init_usermanager(UserManager(db, models.User))
