# -*- coding: utf-8 -*-

from datetime import datetime
from bookreview import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(30))
    password = db.Column(db.String(128))
    reviews = db.relationship("BookReview", backref="user", lazy="dynamic")

    def __init__(self, name="", mail="", plain_password=""):
        self.username = name
        self.email = mail
        self.password = generate_password_hash(plain_password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User> {0}'.format(self.username)

    def __unicode__(self):
        return self.username

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Unicode(64))
    author = db.Column(db.Unicode(32))
    isbn = db.Column(db.String(16), unique=True)
    publish_date = db.Column(db.Date)
    edition = db.Column(db.Integer)
    reviews = db.relationship("BookReview", backref="book", lazy="dynamic")

    def __init__(self, title="", isbn="", publish_date=datetime.now()):
        self.title = title
        self.isbn = isbn
        self.publish_date = publish_date

    def __repr__(self):
        return self.title

    def __unicode__(self):
        return self.title

class BookReview(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review_date = db.Column(db.Date)
    review = db.Column(db.UnicodeText)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    slug = db.Column(db.Unicode(64), unique=True)
    is_draft = db.Column(db.Boolean)

    def __repr__(self):
        return "Review for {0} written by {1}".format(db.session.query(Book) \
            .filter_by(id=self.book_id).first(), \
            unicode(db.session.query(User).filter_by(id=self.user_id).first()))

    def __init__(self):
        self.is_draft = False