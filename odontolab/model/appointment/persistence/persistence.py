from odontolab.model.appointment.appointment import Appointment
from odontolab.model.appointment.persistence.appointmentdao import AppointmentDAO
from odontolab.model.utils.singleton import SingletonMeta


class Persistence(AppointmentDAO, metaclass=SingletonMeta):
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
    
    def queryByPatient(self, patient_id: int) -> tuple[list[Appointment], bool]:
        patientAppointments: list[Appointment] = []

        for appointment in self.__appointments.values():
            if appointment.patient_id == patient_id:
                patientAppointments.append(appointment)

        return  patientAppointments, True
