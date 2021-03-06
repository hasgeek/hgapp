# -*- coding: utf-8 -*-

#: Site title
SITE_TITLE = 'Hasgeek App'
#: Site id (for network bar)
SITE_ID = ''
#: Database backend
SQLALCHEMY_DATABASE_URI = 'postgresql:///hgapp'
#: Secret key
SECRET_KEY = 'make this something random'
#: Cache type
CACHE_TYPE = 'redis'
#: RQ settings
RQ_REDIS_URL = 'redis://localhost:6379/0'
RQ_SCHEDULER_INTERVAL = 1
#: Timezone
TIMEZONE = 'Asia/Kolkata'
#: Lastuser server
LASTUSER_SERVER = 'https://auth.hasgeek.com/'
#: Lastuser client id
LASTUSER_CLIENT_ID = ''
#: Lastuser client secret
LASTUSER_CLIENT_SECRET = ''
#: Lastuser cookie domain
# if hosting multiple apps in subdomains, use '.mydomain.tld'
LASTUSER_COOKIE_DOMAIN = None
#: Mail settings
#: MAIL_FAIL_SILENTLY : default True
#: MAIL_SERVER : default 'localhost'
#: MAIL_PORT : default 25
#: MAIL_USE_TLS : default False
#: MAIL_USE_SSL : default False
#: MAIL_USERNAME : default None
#: MAIL_PASSWORD : default None
#: MAIL_DEFAULT_SENDER : default None
MAIL_FAIL_SILENTLY = False
MAIL_SERVER = 'localhost'
MAIL_DEFAULT_SENDER = 'Hasgeek <test@example.com>'
#: Logging: recipients of error emails
ADMINS = []
#: Log file
LOGFILE = 'error.log'
