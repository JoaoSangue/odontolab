from datetime import date, datetime

class Patient:
    def __init__(self, cpf: str = '', name: str = '', birthdate: str = '', addr: str = '', phone: str = ''):
        self.id: int = 0

        self.cpf: str = cpf
        self.name: str = name
        self.birthdate: date = datetime.strptime(birthdate, "%Y-%m-%d").date()
        self.addr: str = addr
        self.phone: str = phone
    
    def __isValid(self) -> bool:
        # TODO: Consider viability of wrapper class for validating specific strings 
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
        
        return True

    def canBeCreated(self) -> bool:
        return self.__isValid()
