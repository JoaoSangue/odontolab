from odontolab.model.patient.patient import Patient
from odontolab.model.patient.patientdao import PatientDAO
from odontolab.model.utils.singleton import SingletonMeta


class Persistence(PatientDAO, metaclass=SingletonMeta):
    """ Implements a PatientDAO using a dict in memmory
    """

    def __init__(self):
        self.__patients: dict[int, Patient] = dict()
        self.__patients_cpf_index: dict[str, int] = dict()

    def create(self, patient: Patient) -> tuple[Patient, bool]:
        if patient.id not in self.__patients and patient.cpf not in self.__patients_cpf_index:
            patient.id = len(self.__patients) + 1
            self.__patients[patient.id] = patient
            self.__patients_cpf_index[patient.cpf] = patient.id
            return patient, True

        return patient, False
    
    def find(self, cpf: str) -> tuple[Patient, bool]:
        if cpf in self.__patients_cpf_index:
            id = self.__patients_cpf_index[cpf]
            patient = self.__patients[id]
            return patient, True

        return  Patient(), False
