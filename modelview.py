# -*- coding: utf-8 -*-

from flask.ext.admin.contrib.sqla import ModelView 
from flask import redirect, url_for, request
from wtforms import PasswordField
from model import User
from flask.ext import login, admin
from flask.ext.admin import expose, helpers
from forms import LoginForm

class AuthModelView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()

class UserView(ModelView):
    column_list = ("username", "email")

    form_extra_fields = {
        'password': PasswordField('Password')
    }

    def __init__(self, session, **kwargs):
        super(UserView, self).__init__(User, session, **kwargs)

class BackendAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(BackendAdminIndexView, self).inedx()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)

        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))