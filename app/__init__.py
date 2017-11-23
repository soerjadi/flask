# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

# import controller into application
from app.controllers import *


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
