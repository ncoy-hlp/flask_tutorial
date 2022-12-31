import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("FLASK_DATABASE_URI") or \
        'sqlite:///' + os.path.join(basedir, 'site.db')
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("FLASK_EMAIL")
    MAIL_PASSWORD = os.environ.get("FLASK_EMAIL_PASSWORD")