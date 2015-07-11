# -*- coding: utf-8 -*-

from bookreview import app, admin, db
from flask_admin.contrib.sqla import ModelView
from model import User, Book, BookReview
from modelview import UserView

if __name__ == '__main__':
    admin.add_view(UserView(User, db.session))
    admin.add_view(ModelView(Book, db.session))
    admin.add_view(ModelView(BookReview, db.session))
    app.run("0.0.0.0", debug=True)