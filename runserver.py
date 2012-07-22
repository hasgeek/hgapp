#!/usr/bin/env python
from hgapp import app, init_for
from hgapp.models import db
init_for('dev')
db.create_all()
app.run('0.0.0.0', debug=True, port=8000)
