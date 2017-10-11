#!/bin/sh
pybabel extract -F babel.cfg -k _ -k __ -k ngettext -o hgapp/translations/messages.pot .
pybabel update -D hgapp -i hgapp/translations/messages.pot -d hgapp/translations
