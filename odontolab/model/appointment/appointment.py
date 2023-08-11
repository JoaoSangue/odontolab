from datetime import date

class Appointment:
    def __init__(self, patient_id: int, reason: str):
        self.id: int
        self.details: str

        self.patient_id: int = patient_id
        self.date: date = date.today
        self.reason: str = reason
