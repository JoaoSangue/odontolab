from flask import Flask, render_template, url_for
from odontolab.controller.appointment import AppointmentRouter
from odontolab.controller.code import CodeRouter
from odontolab.controller.mainrouter import MainRouter
from odontolab.controller.patient import PatientRouter

from odontolab.controller.router import Router

class Controller(Router):
    """ Controller.
        Configures routes for the application.
    """

    def __init__(self, app: Flask):
        self.__app: Flask = app
    
    def defineRoutes(self):
        router: Router = MainRouter(self.__app)

        router = CodeRouter(router)
        router = PatientRouter(router)
        router = AppointmentRouter(router)

        router.defineRoutes()
