from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# this is for development
app = Flask(__name__)
app.config["SECRET_KEY"] = '547d656f1f3e3983b1a27d7bedd40975'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

# import after app initialization 
# otherwise there is a circular import

from flask_blog import routes