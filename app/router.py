# -*- coding: utf-8 -*-
from app import app
from app.controllers.home_controller import HomeController
from app.controllers.login_controller import LoginController


HomeController.register(app, route_base="/")
LoginController.register(app)

