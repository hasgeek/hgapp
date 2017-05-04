#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from hgapp import app

try:
    port = int(sys.argv[1])
except (IndexError, ValueError):
    port = 8000
app.run('0.0.0.0', port=port)
