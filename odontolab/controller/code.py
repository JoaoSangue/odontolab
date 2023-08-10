from flask import Flask, abort, render_template

def defineCodeRoutes(app: Flask):
    """ Define code's routes
    """

    # View routes

    @app.get('/code/')
    def current_service_code_view():
        """ View for querying current service code priority
        """
        # abort(501)
        return render_template('codes.html')

    @app.get('/code/new/')
    def next_service_code_view():
        """ View for generating a new code for patient to be served
        """
        abort(501)
