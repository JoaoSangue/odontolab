from __future__ import annotations
from datetime import date

class Appointment:
    def __init__(self, patient_id: int = 0, reason: str = ''):
        self.id: int = 0
        self.details: str = ''

        self.patient_id: int = patient_id
        self.date: date = date.today()
        self.reason: str = reason

    def __isValid(self) -> bool:
        if self.patient_id <= 0:
            print('Invalid patient ID for appointment')
            return False
        
        if self.reason.strip() == '':
            print('Invalid reason for appointment')
            return False
        
        return True

    def canBeCreated(self) -> bool:
        return self.__isValid()

    def canBeUpdated(self) -> bool:
        if not self.__isValid():
            return False

        if self.details.strip() == '':
            print('Invalid details for appointment')
            return False
        
        return True
