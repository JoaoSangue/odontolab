from odontolab.model.patient.patient import Patient
from odontolab.model.patient.patientdao import PatientDAO


class Persistence(PatientDAO):
    """ Implements a PatientDAO using a dict in memmory
    """

    def __init__(self):
        self.__patients: dict[int, Patient] = dict()

    def create(self, patient: Patient) -> tuple[Patient, bool]:
        if patient.id not in self.__patient:
            patient.id = len(self.__patients) + 1
            self.__patients[patient.id] = patient
            return patient, True

        return patient, False
    
    def findByCPF(self, cpf: str) -> tuple[Patient, bool]:
        for patient in self.__appointments.values():
            if patient.cpf == cpf:
                return patient

        return  Patient('', '', 0, '', ''), True
