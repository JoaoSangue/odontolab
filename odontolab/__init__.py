from flask import Flask, abort, render_template
from markupsafe import escape

from odontolab.controller.controller import Controller

app = Flask(__name__)


controller = Controller(app)
controller.defineRoutes()

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)