# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo


class LoginForm(Form):
    email = TextField("Email Address", [Email(), Required(message = "Forgot your email address?")])
    password = PasswordField("Password", [Required(message = "Password cannot be empty")])
