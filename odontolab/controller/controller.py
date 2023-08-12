from flask import Flask, render_template, url_for
from odontolab.controller.appointment import AppointmentRouter
from odontolab.controller.code import CodeRouter
from odontolab.controller.patient import PatientRouter

from odontolab.controller.router import Router

class Controller(Router):
    def __init__(self, app: Flask):
        self.__app: Flask = app
        self.__routers: list[Router] = [
            CodeRouter(app),
            PatientRouter(app),
            AppointmentRouter(app)
        ]
    
    def defineRoutes(self):
        @self.__app.route('/')
        def index():
            """ Home page view
            """

            routes = []
            for rule in self.__app.url_map.iter_rules():

                # Exclude rules that require parameters and rules you can't open in a browser
                defaults = rule.defaults if rule.defaults is not None else ()
                arguments = rule.arguments if rule.arguments is not None else ()
                has_no_empty_params = len(defaults) >= len(arguments)

                if "GET" in rule.methods and has_no_empty_params:
                    url = url_for(rule.endpoint, **(rule.defaults or {}))
                    routes.append(url)

            return render_template('index.html', routes=routes)

        for router in self.__routers:
            router.defineRoutes()