from flask import Flask, render_template, request, session
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
     UserMixin, RoleMixin, login_required

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/db.sqlite'
app.config['DEFAULT_MAIL_SENDER'] = 'info@site.com'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_CONFIRMABLE'] = True
app.config['SECURITY_RECOVERABLE'] = True
app.config.from_object('boiler.email')

# Setup mail extension
mail = Mail(app)

# Create database connection object
db = SQLAlchemy(app)
