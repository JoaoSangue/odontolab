from odontolab.model.patient.patient import Patient
from odontolab.model.patient.patientdao import PatientDAO
from odontolab.model.patient.persistence import Persistence


class PatientService:
    """ PatientService.
        Service proxying for PatientDAO.
        Works as a Facade hiding what needs to be done, before persisting data.
    """   

    __persistence: PatientDAO = Persistence()

    def __new__(cls):
        raise TypeError(f"'{cls.__name__}' is static and cannot be instantiated")

    @classmethod
    def createPatient(cls, patient: Patient) -> tuple[Patient, bool]:
        if not patient.canBeCreated():
            return patient, False
        return cls.__persistence.create(patient)

    @classmethod
    def findPatientByCPF(cls, cpf: str) -> tuple[Patient, bool]:
        return cls.__persistence.find(cpf)