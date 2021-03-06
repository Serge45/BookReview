# -*- coding: utf-8 -*-

from flask import Flask, render_template, abort
from flask_admin import Admin
from flask.ext import login
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'sdghir035nvawihegovnv0-64y jioj'

db = SQLAlchemy(app)
from model import User, BookReview, Book

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

@app.route('/<username>/')
def reviews(username):
    user = db.session.query(User).filter_by(username=username).first()
    if user:
        book_reviews = []

        for r in user.reviews:
            book_reviews.append(((db.session.query(Book).get(r.book_id)), r.slug))
        return render_template('query_result.html', result=book_reviews,
            username=user.username)
    return abort(404)

@app.route('/<username>/<slug>/')
def review(username, slug):
    user = db.session.query(User).filter_by(username=username).first()
    if user:
        review = db.session.query(BookReview).filter_by(slug=slug).first()

        if review:
            book = db.session.query(Book).get(review.book_id)

            if book:
                return render_template('post.html', title=book.title, 
                    review=review)
    return abort(404)


from modelview import BackendAdminIndexView

admin = Admin(app, 'Book review admin site', index_view=BackendAdminIndexView())
init_login()