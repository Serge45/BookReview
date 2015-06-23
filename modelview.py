# -*- coding: utf-8 -*-

from flask.ext.admin.contrib.sqla import ModelView 
from flask import redirect, url_for, request, render_template
from wtforms import PasswordField
from flask.ext import login, admin
from flask.ext.admin import expose, helpers
from forms import LoginForm

class AuthModelView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()

class UserView(AuthModelView):
    column_list = ("username", "email")

    form_extra_fields = {
        'password': PasswordField('Password')
    }

    def __init__(self, type_name, session, **kwargs):
        super(UserView, self).__init__(type_name, session, **kwargs)

class BackendAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(BackendAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)

        if form.validate_login():
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))

        return render_template("login.html", form=form)