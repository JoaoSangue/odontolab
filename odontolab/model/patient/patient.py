from datetime import date

class Patient:
    def __init__(self, cpf: str, name: str, birthdate: int, addr: str, phone: str):
        self.id: int

        self.cpf: str = cpf
        self.name: str = name
        self.birthdate: date = date.fromtimestamp(birthdate)
        self.addr: str = addr
        self.phone: str = phone
    
    def __isValid(self) -> bool:
        if self.cpf.strip() == '':
            print('Invalid cpf for patient')
            return False

        if self.name.strip() == '':
            print('Invalid name for patient')
            return False

        if self.addr.strip() == '':
            print('Invalid address for patient')
            return False

        if self.phone.strip() == '':
            print('Invalid phone for patient')
            return False

    def canBeCreated(self) -> bool:
        return self.__isValid()
