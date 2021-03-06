# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)

import router


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
