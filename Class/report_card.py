from student import Student

class ReportCard(Student):
    def __init__(self, name, roll_number, subjects):
        super().__init__(name, roll_number) 
        self.__subjects = {subject.get_name(): subject.get_max_marks() for subject in subjects}
        self.__marks = {subject.get_name(): None for subject in subjects}

    def enter_marks(self, marks):
        for subject, mark in marks.items():
            self.__marks[subject] = mark

    def calculate_total(self):
        return sum(mark for mark in self.__marks.values() if mark is not None)

    def calculate_percentage(self):
        total = self.calculate_total()
        max_total = sum(self.__subjects.values())
        return (total / max_total)*100

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "D"

    def generate_report(self):
        print(f"\nReport for {self.get_name()} (Roll No: {self.get_roll_number()})")
        for subject, mark in self.__marks.items():
            print(f"{subject}: {mark}/100")
        print(f"Total Marks: {self.calculate_total()}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")
        print(f"Grade: {self.calculate_grade()}")
