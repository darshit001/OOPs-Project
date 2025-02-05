class Subject:
    def __init__(self,name,max_marks):
        self.__name = name
        self.__max_marks = max_marks

    def get_name(self):
        return self.__name

    def get_max_marks(self):
        return self.__max_marks
