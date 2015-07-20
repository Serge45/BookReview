# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_admin import Admin
from flask.ext import login
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'sdghir035nvawihegovnv0-64y jioj'

db = SQLAlchemy(app)
from model import User, BookReview

def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

@app.route('/')
def index():
    reviews = db.session.query(BookReview).all()
    return render_template("index.html", reviews=reviews)

from modelview import BackendAdminIndexView

admin = Admin(app, 'Book review admin site', index_view=BackendAdminIndexView())
init_login()