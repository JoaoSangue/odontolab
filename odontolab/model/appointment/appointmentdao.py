import abc

from odontolab.model.patient.patient import Patient
from odontolab.model.appointment.appointment import Appointment


class AppointmentDAO(metaclass=abc.ABCMeta):
    """ DAO interface for Appointment.
        Defines methods for persisting and accessing appointments.
    """

    @abc.abstractmethod
    def create(self, appointment: Appointment) -> tuple[Appointment, bool]:
        return
    
    @abc.abstractmethod
    def update(self, appointment: Appointment) -> tuple[Appointment, bool]:
        return

    @abc.abstractmethod
    def queryByPatient(self, patient: Patient) -> tuple[list[Appointment], bool]:
        return

