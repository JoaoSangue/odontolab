from flask import Flask, abort, redirect, render_template, url_for

from odontolab.controller.router import Router

class AppointmentRouter(Router):
    def __init__(self, app: Flask):
        self.__app = app

    def defineRoutes(self):

        @self.__app.get('/appointments/')
        def appointments_queue_view():
            """ Renders view for querying queue of appointments
            """

            abort(501)
            render_template('appointments.html')

        @self.__app.post('/appointments/next')
        def call_next_appointments_from_queue():
            """ Call next scheduled patient
            """

            abort(501)
            return redirect(url_for('patient_appointments_view'))


        @self.__app.get('/patients/<int:id>/appointments/new/')
        def appointment_creation_view():
            """ Renders view for creating new appointment for a patient
            """
            
            abort(501)
            return render_template('new_appointment.html')

        @self.__app.post('/patients/<int:id>/appointments/new/')
        def create_appointment():
            """ Creates new appointment for a patient
            """
            
            abort(501)
            return render_template('new_appointment.html')
        

        @self.__app.get('/patients/<int:id>/appointments/')
        def patient_appointments_view():
            """ Renders view for querying all of a patients' appointments
            """

            abort(501)
            return render_template('patient_appointments.html')


        @self.__app.put('/patients/<int:patient_id>/appointments/<int:appointment_id>')
        def update_patient_appointment():
            """ Updates a patients' appointment
            """

            abort(501)
            return redirect(url_for('patient_appointments_view'))
