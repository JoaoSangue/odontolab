class Code:
    def __init__(self) -> None:
        self.__value = 0;
    
    def next(self) -> int:
        self.__value = self.__value + 1
        return self.__value
    
    def current(self) -> int:
        return self.__value