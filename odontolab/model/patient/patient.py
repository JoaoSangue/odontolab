from datetime import date

class Patient:
    def __init__(self, cpf: str, name: str, birthdate: int, addr: str, phone: str):
        self.id: int

        self.cpf: str = cpf
        self.name: str = name
        self.birthdate: date = date.fromtimestamp(birthdate)
        self.addr: str = addr
        self.phone: str = phone
    
