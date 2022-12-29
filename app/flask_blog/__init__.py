from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

# this is for development
app = Flask(__name__)
app.config["SECRET_KEY"] = '547d656f1f3e3983b1a27d7bedd40975'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config["MAIL_USERNAME"] = os.environ.get("FLASK_EMAIL")
app.config["MAIL_PASSWORD"] = os.environ.get("FLASK_EMAIL_PASSWORD")
mail = Mail(app)

# import after app initialization 
# otherwise there is a circular import

from flask_blog import routes