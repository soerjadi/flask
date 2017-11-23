# -*- coding: utf-8 -*-
from flask_classy import FlaskView


class HomeController(FlaskView):
    """

    """
    def __init__(self):
        return

    def index(self):
        return "hello"


# HomeController.register(app)
# @app.route("/")
# def index():
#     return render_template_string("hello")
