from datetime import date

class Appointment:
    def __init__(self, patient_id: int, reason: str):
        self._id: int
        self.details: str

        self._patient_id: int = patient_id
        self.date: date = date.today
        self.reason: str = reason

    # TODO: Create a DAO class for persistence and make implementation in memmory