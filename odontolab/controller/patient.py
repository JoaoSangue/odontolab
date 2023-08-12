from flask import Flask, abort, flash, redirect, render_template, request, url_for

from odontolab.controller.router import Router
from odontolab.model.patient import PatientService, Patient

class PatientRouter(Router):
    def __init__(self, app: Flask):
        self.__app = app

    def defineRoutes(self):

        @self.__app.get('/patients/')
        def patient_search_view():
            """ Renders view for querying patients by their CPF
            """

            return render_template('patients.html')

        @self.__app.post('/patients/')
        def search_patient():
            """ Searches for a patient by CPF
            """

            cpf = request.form['cpf']
            patient, found = PatientService.findPatientByCPF(cpf)
            if found:
                return redirect(url_for('appointment_creation_view', id=patient.id))
            return redirect(url_for('patient_creation_view', cpf=cpf))


        @self.__app.get('/patients/new/')
        def patient_creation_view():
            """ Renders view for creating new patients
            """
    
            cpf = request.args.get('cpf')
            return render_template('new_patient.html', cpf=cpf)

        @self.__app.post('/patients/new/')
        def create_patient():
            """ Create new patient
            """

            form = request.form.to_dict(True)
            patient = Patient(**form)
            patient, ok = PatientService.createPatient(patient)
            if ok:
                return redirect(url_for('appointment_creation_view', id=patient.id))
            
            # TODO: Fix error handling. It's showing same message for persistence errors
            error = 'Campos inválidos ou vazios no formulário'
            return render_template('new_patient.html', error=error)


