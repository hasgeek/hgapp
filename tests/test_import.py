# -*- coding: utf-8 -*-

from flask import Flask

def test_import():
    from hgapp import app
    assert isinstance(app, Flask)
