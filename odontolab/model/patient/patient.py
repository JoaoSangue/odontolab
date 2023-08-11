from __future__ import annotations
from datetime import date

from odontolab.model.patient.persistence import PatientDAO, Persistence

class Patient:
    __persistence: PatientDAO = Persistence()

    def __init__(self, cpf: str, name: str, birthdate: int, addr: str, phone: str):
        self.id: int

        self.cpf: str = cpf
        self.name: str = name
        self.birthdate: date = date.fromtimestamp(birthdate)
        self.addr: str = addr
        self.phone: str = phone
    
    def __isValid(self) -> bool:
        if self.cpf.strip() == '':
            print('Invalid cpf for patient')
            return False

        if self.name.strip() == '':
            print('Invalid name for patient')
            return False

        if self.addr.strip() == '':
            print('Invalid address for patient')
            return False

        if self.phone.strip() == '':
            print('Invalid phone for patient')
            return False

    def create(self) -> tuple[Patient, bool]:
        if not self.__isValid():
            return self, False

        return self.__persistence.create(self)

    def findByCPF(self, cpf: str) -> tuple[Patient, bool]:
        return self.__persistence.find(cpf)