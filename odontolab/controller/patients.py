from flask import Flask, abort

def definePatientsRoutes(app: Flask):
    """ Define patients' routes
    """

    # View routes

    @app.get('/patients/')
    def patient_search_view():
        """ View for querying pacients by their CPF
        """
        abort(501)

    @app.get('/patients/new/')
    def patient_creation_view():
        """ View for creating new pacients
        """
        abort(501)

    @app.get('/patients/:id/appointments/')
    def patient_appointments_view():
        """ View for querying all of a pacients' appointments
        """
        abort(501)

    @app.get('/patients/:id/appointments/new/')
    def appointment_creation_view():
        """ View for creating new appointment for pacients
        """
        abort(501)
