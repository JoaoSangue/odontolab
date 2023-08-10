from flask import Flask, abort
from .code import _defineCodeRoutes
from .patient import _definePatientsRoutes
from .appointment import _defineAppointmentsRoutes

# TODO: Create classes for managing routes
def defineRoutes(app: Flask):
    """ Define all app routes
    """

    _defineCodeRoutes(app)
    _definePatientsRoutes(app)
    _defineAppointmentsRoutes(app)
