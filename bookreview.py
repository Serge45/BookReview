# -*- coding: utf-8 -*-

from flask import Flask
from flask_admin import Admin
from flask.ext import login
from flask.ext.sqlalchemy import SQLAlchemy
#from modelview import BackendAdminIndexView

app = Flask(__name__)

def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'sdghir035nvawihegovnv0-64y jioj'

db = SQLAlchemy(app)
admin = Admin(app)#, 'Book review admin site', index_view=BackendAdminIndexView())
init_login()