# -*- coding: utf-8 -*-

from datetime import datetime
from bookreview import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(30))
    password = db.Column(db.String(128))

    def __init__(self, name="", mail="", plain_password=""):
        self.username = name
        self.email = mail
        self.password = generate_password_hash(plain_password)

    def __repr__(self):
        return '<User> {0}'.format(self.username)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.username

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Unicode(64))
    author = db.Column(db.Unicode(32))
    isbn = db.Column(db.String(16), unique=True)
    publish_date = db.Column(db.Date)
    edition = db.Column(db.Integer)

    def __init__(self, title="", isbn="", publish_date=datetime.now()):
        self.title = title
        self.isbn = isbn
        self.publish_date = publish_date

    def __repr__(self):
        return '<Book> {0}'.format(self.title)

class BookReview(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review = db.Column(db.UnicodeText)