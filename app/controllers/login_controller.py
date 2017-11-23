# -*- coding: utf-8 -*-
from flask import request, render_template
from app import app
# Import Login form
from app.forms.login_form import LoginForm


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():

        print("login")

    return render_template("login.html", form=form)
