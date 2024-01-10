#!/usr/bin/env python3

from flask import Flask
from flask_sqlachemy import SQLAlchemy
from flask_migrate import migrate

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    app.run(port=5555, debug=True)
