from flask import Flask, abort
from .code import defineCodeRoutes
from .patients import definePatientsRoutes
from .appointments import defineAppointmentsRoutes

def defineRoutes(app: Flask):
    """ Define all app routes
    """

    defineCodeRoutes(app)
    definePatientsRoutes(app)
    defineAppointmentsRoutes(app)
