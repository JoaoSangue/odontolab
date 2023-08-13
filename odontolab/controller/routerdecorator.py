from flask import Flask
from odontolab.controller.router import Router


class RouterDecorator(Router):
    _router: Router = None

    def __init__(self, router: Router) -> None:
        self._router: Router = router
        self._app: Flask = router._app

    def defineRoutes(self):
        self._router.defineRoutes()