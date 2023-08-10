from flask import Flask, abort

def defineAppointmentsRoutes(app: Flask):
    """ Define appointments' routes
    """

    # View routes

    @app.get('/appointments/')
    def appointments_queue_view():
        """ View for querying queue of appointments
        """
        abort(501)
