from queue import SimpleQueue as Queue

from ..code import Code
from ..appointment import Appointment

class Clinic:
    def __init__(self) -> None:
        self.__currently_serving_code: Code = Code()
        self.__last_generated_code: Code = Code()

        self.__appointments: Queue[Appointment] = Queue()

    def currentlyServing(self) -> int:
        return self.__currently_serving_code.current()

    def callNextServiceCode(self) -> int:
        return self.__currently_serving_code.next()

    def generateNextServiceCode(self) -> int:
        return self.__last_generated_code.next()

    def callNextAppointment(self) -> Appointment:
        if not self.__appointments.empty():
            return self.__appointments.get()
        return Appointment(0, '')

    def queueAppointment(self, patient_id: int, reason: str) -> None:
        newAppointment = Appointment(patient_id, reason)
        self.__appointments.put(newAppointment)
