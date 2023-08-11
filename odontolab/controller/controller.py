from flask import Flask, abort
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

            return 'Index Page'

        for router in self.__routers:
            router.defineRoutes()