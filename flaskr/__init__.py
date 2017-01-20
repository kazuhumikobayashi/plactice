from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('flaskr.config')

db = SQLAlchemy(app)

import flaskr.views
