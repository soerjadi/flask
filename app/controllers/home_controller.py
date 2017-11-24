# -*- coding: utf-8 -*-
from flask_classy import FlaskView
from flask import render_template


class HomeController(FlaskView):
    """
    Home Controller
    """
    def __init__(self):
        return

    def index(self):
        return render_template("index.html", title="Home")
