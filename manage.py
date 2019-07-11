#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hgapp
import hgapp.forms as forms
import hgapp.models as models
import hgapp.views as views
from coaster.manage import init_manager
from hgapp import app
from hgapp.models import db

if __name__ == '__main__':
    db.init_app(app)
    manager = init_manager(
        app, db, hgapp=hgapp, models=models, forms=forms, views=views
    )
    manager.run()
