from flask import Flask

from odontolab.controller.controller import Controller

app = Flask(__name__)


controller = Controller(app)
controller.defineRoutes()
