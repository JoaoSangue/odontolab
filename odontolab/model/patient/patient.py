from datetime import date

class Patient:
    def __init__(self, cpf: str, name: str, birthdate: int, addr: str, phone: str):
        self._id: int

        self.cpf: str = cpf
        self.name: str = name
        self.birthdate: date = date.fromtimestamp(birthdate)
        self.addr: str = addr
        self.phone: str = phone
    
    # TODO: Create a DAO class for persistence and make implementation in memmory
