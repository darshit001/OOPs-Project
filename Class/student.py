from abc import ABC,abstractmethod

class Student(ABC):
    def __init__(self, name, roll_number):
        self.__name = name
        self.__roll_number = roll_number
       
    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    @abstractmethod
    def generate_report(self):
        pass
