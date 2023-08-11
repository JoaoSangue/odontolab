import abc

from odontolab.model.patient.patient import Patient


class PatientDAO(metaclass=abc.ABCMeta):
    """ DAO interface for Patient.
        Defines methods for persisting and accessing patients.
    """

    @abc.abstractmethod
    def create(self, patient: Patient) -> tuple[Patient, bool]:
        return

    @abc.abstractmethod
    def find(self, cpf: str) -> tuple[Patient, bool]:
        return
