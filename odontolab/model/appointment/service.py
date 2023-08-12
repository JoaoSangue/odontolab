from odontolab.model.appointment.appointment import Appointment
from odontolab.model.appointment.persistence import Persistence
from odontolab.model.appointment.appointmentdao import AppointmentDAO


class AppointmentService:
    __persistence: AppointmentDAO = Persistence()

    def __new__(cls):
        raise TypeError(f"'{cls.__name__}' is static and cannot be instantiated")

    @classmethod
    def createAppointment(cls, appointment: Appointment) -> tuple[Appointment, bool]:
        if not appointment.canBeCreated():
            return appointment, False

        return cls.__persistence.create(appointment)

    @classmethod
    def updateAppointment(cls, appointment: Appointment) -> tuple[Appointment, bool]:
        if not appointment.canBeUpdated():
            return appointment, False

        return cls.__persistence.update(appointment)

    @classmethod
    def findAppointmentByPatient(cls, patient_id: int) -> tuple[list[Appointment], bool]:
        return cls.__persistence.queryByPatient(patient_id)