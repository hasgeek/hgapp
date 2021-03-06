# -*- coding: utf-8 -*-

# The imports in this file are order-sensitive



from flask import Flask
from flask_migrate import Migrate
from flask_rq2 import RQ

import coaster.app
from baseframe import Version, assets, baseframe
from flask_lastuser import Lastuser
from flask_lastuser.sqlalchemy import UserManager

from ._version import __version__

version = Version(__version__)

# First, make an app

app = Flask(__name__, instance_relative_config=True)
lastuser = Lastuser()
rq = RQ()

# Second, import the models and views

from . import models, views  # NOQA  # isort:skip
from .models import db  # isort:skip

# Third, setup baseframe and assets

assets['hgapp.js'][version] = 'js/app.js'
assets['hgapp.css'][version] = 'css/app.css'

# Configure the app
coaster.app.init_app(app)
db.init_app(app)
db.app = app
migrate = Migrate(app, db)
rq.init_app(app)
baseframe.init_app(app, requires=['baseframe-bs3', 'hgapp'])
lastuser.init_app(app)
lastuser.init_usermanager(UserManager(db, models.User))
