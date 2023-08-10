from flask import Flask, abort, redirect, render_template, url_for

def _definePatientsRoutes(app: Flask):
    """ Define patients' routes
    """

    @app.get('/patients/')
    def patient_search_view():
        """ Renders view for querying patients by their CPF
        """

        abort(501)

    @app.post('/patients/')
    def search_patient():
        """ Searches for a patient by CPF
        """

        # if found:
        #     return redirect(url_for('appointment_creation_view', id=found.id))
        # return redirect(url_for('patient_creation_view'))
        abort(501)


    @app.get('/patients/new/')
    def patient_creation_view():
        """ Renders view for creating new patients
        """

        abort(501)
        return render_template('new_patient.html')

    @app.post('/patients/new/')
    def create_patient():
        """ Create new patient
        """

        abort(501)
        return redirect(url_for('appointment_creation_view'))

