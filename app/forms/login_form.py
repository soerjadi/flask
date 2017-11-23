# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField("Email Address", [Email(), DataRequired(message="Forgot your email address?")])
    password = PasswordField("Password", [DataRequired(message="Password cannot be empty")])
