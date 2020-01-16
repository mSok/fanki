import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from models import *
# Init Flask
app = Flask(__name__)

basedir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

cards.db.init_app(app)
app.app_context().push()

cards.db.create_all()
