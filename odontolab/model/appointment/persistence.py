from odontolab.model.appointment.appointment import Appointment
from odontolab.model.appointment.appointmentdao import AppointmentDAO
from odontolab.model.patient.patient import Patient


class Persistence(AppointmentDAO):
    """ Implements a AppointmentDAO using a dict in memmory
    """

    def __init__(self):
        self.__appointments: dict[int, Appointment] = dict()

    def create(self, appointment: Appointment) -> tuple[Appointment, bool]:
        if appointment.id not in self.__appointments:
            appointment.id = len(self.__appointments) + 1
            self.__appointments[appointment.id] = appointment
            return appointment, True

        return appointment, False
    
    def update(self, appointment: Appointment) -> tuple[Appointment, bool]:
        if appointment.id in self.__appointments:
            self.__appointments[appointment.id] = appointment
            return appointment, True

        return appointment, False
    
    def queryByPatient(self, patient: Patient) -> tuple[list[Appointment], bool]:
        patientAppointments: list[Appointment] = []

        for appointment in self.__appointments.values():
            if appointment.patient_id == patient.id:
                patientAppointments.append(appointment)

        return  patientAppointments, True
