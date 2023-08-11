from __future__ import annotations
from datetime import date

from odontolab.model.appointment.persistence import AppointmentDAO
from odontolab.model.patient.persistence import Persistence


class Appointment:
    __persistence: AppointmentDAO = Persistence()

    def __init__(self, patient_id: int, reason: str):
        self.id: int
        self.details: str

        self.patient_id: int = patient_id
        self.date: date = date.today
        self.reason: str = reason

    def __validate(self) -> bool:
        if self.patient_id <= 0:
            print('Invalid patient ID for appointment')
            return False
        
        if self.reason.strip() == '':
            print('Invalid reason for appointment')
            return False

    def create(self) -> tuple[Appointment, bool]:
        if not self.validate():
            return self, False

        return self.__persistence.create(self)

    def update(self) -> tuple[Appointment, bool]:
        if not self.validate():
            return self, False

        if self.details.strip() == '':
            print('Invalid details for appointment')
            return self, False

        return self.__persistence.update(self)

    def queryByPatient(self, patient_id: int) -> tuple[list[Appointment], bool]:
        return self.__persistence.queryByPatient(self, patient_id)
