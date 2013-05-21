#!/usr/bin/env python
import sys
from hgapp import app, init_for
from hgapp.models import db
init_for('dev')
db.create_all()

try:
    port = int(sys.argv[1])
except (IndexError, ValueError):
    port = 8000
app.run('0.0.0.0', port=port, debug=True)
