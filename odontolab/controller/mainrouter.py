from flask import Flask, render_template, url_for
from odontolab.controller.router import Router


class MainRouter(Router):
    def __init__(self, app: Flask) -> None:
        self._app = app

    def defineRoutes(self) -> None:
        @self._app.route('/')
        def index():
            """ Home page view listing main routes
            """

            routes = []
            for rule in self._app.url_map.iter_rules():

                # Exclude rules that require parameters and rules you can't open in a browser
                defaults = rule.defaults if rule.defaults is not None else ()
                arguments = rule.arguments if rule.arguments is not None else ()
                has_no_empty_params = len(defaults) >= len(arguments)

                if "GET" in rule.methods and has_no_empty_params:
                    url = url_for(rule.endpoint, **(rule.defaults or {}))
                    routes.append(url)

            return render_template('index.html', routes=routes)
