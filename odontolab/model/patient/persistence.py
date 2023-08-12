from odontolab.model.patient.patient import Patient
from odontolab.model.patient.patientdao import PatientDAO
from odontolab.model.utils.singleton import SingletonMeta


class Persistence(PatientDAO, metaclass=SingletonMeta):
    """ Implements a PatientDAO using a dict in memmory
    """

    def __init__(self):
        self.__patients: dict[int, Patient] = dict()

    def create(self, patient: Patient) -> tuple[Patient, bool]:
        if patient.id not in self.__patients:
            patient.id = len(self.__patients) + 1
            self.__patients[patient.id] = patient
            return patient, True

        return patient, False
    
    def find(self, cpf: str) -> tuple[Patient, bool]:
        for patient in self.__patients.values():
            if patient.cpf == cpf:
                return patient, True

        return  Patient('', '', 0, '', ''), False
