from flask import Flask, abort, redirect, render_template, url_for

def _defineAppointmentsRoutes(app: Flask):
    """ Define appointments' routes
    """

    @app.get('/appointments/')
    def appointments_queue_view():
        """ Renders view for querying queue of appointments
        """

        abort(501)
        render_template('appointments.html')

    @app.post('/appointments/next')
    def call_next_appointments_from_queue():
        """ Call next scheduled patient
        """

        abort(501)
        return redirect(url_for('patient_appointments_view'))


    @app.get('/patients/:id/appointments/new/')
    def appointment_creation_view():
        """ Renders view for creating new appointment for a patient
        """
        
        abort(501)
        return render_template('new_appointment.html')

    @app.post('/patients/:id/appointments/new/')
    def create_appointment():
        """ Creates new appointment for a patient
        """
        
        abort(501)
        return render_template('new_appointment.html')
    

    @app.get('/patients/:id/appointments/')
    def patient_appointments_view():
        """ Renders view for querying all of a patients' appointments
        """

        abort(501)
        return render_template('patient_appointments.html')


    @app.put('/patients/:id/appointments/:id')
    def update_patient_appointment():
        """ Updates a patients' appointment
        """

        abort(501)
        return redirect(url_for('patient_appointments_view'))
