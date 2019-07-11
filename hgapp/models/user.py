# -*- coding: utf-8 -*-

from flask_lastuser.sqlalchemy import UserBase2

from . import db

__all__ = ['User']


class User(UserBase2, db.Model):
    __tablename__ = 'user'
