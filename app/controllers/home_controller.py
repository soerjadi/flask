# -*- coding: utf-8 -*-
from app import app
from flask import render_template_string


@app.route("/")
def index():
    return render_template_string("hello")
