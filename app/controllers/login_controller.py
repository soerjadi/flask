# -*- coding: utf-8 -*-
from flask import request, render_template
from flask_classy import FlaskView, route
# Import Login form
from app.forms.login_form import LoginForm


class LoginController(FlaskView):
    """
    Handle login
    """
    route_base = "/login"

    def __init__(self):
        return

    @route("", methods=["GET", "POST"])
    def index(self):
        form = LoginForm(request.form)

        if form.validate_on_submit():
            print("login")

        return render_template("login.html", form=form)
