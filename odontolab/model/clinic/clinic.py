from queue import SimpleQueue as Queue

from odontolab.model.code import Code
from odontolab.model.appointment import Appointment


class Clinic():
    __currently_serving_code: Code = Code()
    __last_generated_code: Code = Code()

    __appointments: Queue[Appointment] = Queue()

    def __new__(cls):
        raise TypeError(f"'{cls.__name__}' is static and cannot be instantiated")

    @classmethod
    def currentlyServing(cls) -> int:
        return cls.__currently_serving_code.current()

    @classmethod
    def callNextServiceCode(cls) -> int:
        return cls.__currently_serving_code.next()

    @classmethod
    def generateNextServiceCode(cls) -> int:
        return cls.__last_generated_code.next()

    @classmethod
    def callNextAppointment(cls) -> tuple[Appointment, bool]:
        if cls.__appointments.empty():
            return Appointment(0, ''), False
        return cls.__appointments.get(), True

    @classmethod
    def queueAppointment(cls, patient_id: int, reason: str) -> bool:
        appointment, ok = Appointment(patient_id, reason).save()
        if not ok:
            return False
        
        cls.__appointments.put(appointment)
        return True
