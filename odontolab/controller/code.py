from flask import redirect, render_template, url_for

from odontolab.controller.routerdecorator import RouterDecorator
from odontolab.model.clinic import Clinic

class CodeRouter(RouterDecorator):
    def defineRoutes(self):
        @self._router._app.get('/code/')
        def current_service_code_view():
            """ Renders view for querying current service code priority
            """

            code = Clinic.currentlyServing()
            return render_template('codes.html', code=code)

        @self._router._app.post('/code/next/')
        def call_next_service_code():
            """ Call next service code from queue
            """

            Clinic.callNextServiceCode()
            return redirect(url_for('current_service_code_view'))


        @self._router._app.get('/code/new/')
        def next_service_code_view():
            """ Renders view for generating a new code for patient to be served
            """

            return render_template('new_code.html')

        @self._router._app.post('/code/new/')
        def generate_next_service_code():
            """ Generate new service code and renders on view
            """

            code = Clinic.generateNextServiceCode()
            return render_template('new_code.html', code=code)

        self._router.defineRoutes()
    