#!/usr/bin/env python

from coaster.manage import init_manager

import hgapp
import hgapp.models as models
import hgapp.forms as forms
import hgapp.views as views
from hgapp.models import db
from hgapp import app, init_for


if __name__ == '__main__':
    db.init_app(app)
    manager = init_manager(app, db, init_for, hgapp=hgapp, models=models, forms=forms, views=views)
    manager.run()
