HasGeek App Boilerplate
=======================

[![Build status](https://secure.travis-ci.org/hasgeek/hgapp.svg)](https://travis-ci.org/hasgeek/hgapp) [![Coverage Status](https://coveralls.io/repos/hasgeek/hgapp/badge.svg)](https://coveralls.io/r/hasgeek/hgapp)

Base template for an app that uses Lastuser, Baseframe and Coaster with Flask and SQLAlchemy. Supports Python 3+ only.

Setup
-----

1. Clone this repository into your development environment.
2. Create a Python 3 virtualenv and activate it.
3. Install requirements:
    * `pip install -r requirements.txt`
    * `pip install -r test_requirements.txt`
    * `pip install -r dev_requirements.txt`
4. Run `pre-commit install`
5. Customise the repo by finding and replacing _all_ mentions of `hgapp` with your desired name.
6. Run `python manage.py db init` to create a template for database migrations.

This boilerplate uses Compass for custom stylesheets. Stylesheets are located in `hgapp/static/sass` and may be rebuilt with `compass compile`. To rebuild automatically, use `compass watch`.
