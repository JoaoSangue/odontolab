from flask import Flask

from odontolab.controller import Controller, Router

app = Flask(__name__)

controller: Router = Controller(app)
controller.defineRoutes()
