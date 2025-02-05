from abc import ABC, abstractmethod

# LSP: Abstract class ensures subclasses like ReportCard can replace this without altering behavior
# ISP: Only necessary methods are declared (generate_report), no extra unused methods
# SRP: This class is responsible for managing student details (name, roll number)
class Student(ABC):  
    def __init__(self, name, roll_number):
        self.__name = name
        self.__roll_number = roll_number
       
    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    # ISP: Abstract method ensures subclasses must implement only what's relevant
    @abstractmethod
    def generate_report(self):
        pass


# SRP: This class focuses solely on representing subject details
class Subject:
    def __init__(self, name, max_marks):
        self.__name = name
        self.__max_marks = max_marks

    def get_name(self):
        return self.__name

    def get_max_marks(self):
        return self.__max_marks


# LSP: Inherits from Student and can be used interchangeably with it
# SRP: Handles the logic for report cards (marks, total, percentage, grade)
class ReportCard(Student):  
    def __init__(self, name, roll_number, subjects):
        super().__init__(name, roll_number)
        # OCP: Subjects and marks are stored dynamically; new subjects can be added without modifying code
        self.__subjects = {subject.get_name(): subject.get_max_marks() for subject in subjects}
        self.__marks = {subject.get_name(): None for subject in subjects}

    # SRP: Manages the logic for entering marks
    def enter_marks(self, marks):
        for subject, mark in marks.items():
            self.__marks[subject] = mark

    # SRP: Calculates total marks
    def calculate_total(self):
        return sum(mark for mark in self.__marks.values() if mark is not None)

    # SRP: Calculates percentage
    def calculate_percentage(self):
        total = self.calculate_total()
        max_total = sum(self.__subjects.values())
        return (total / max_total) * 100

    # SRP: Determines grade based on percentage
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

    # LSP: Overrides abstract method from Student and works seamlessly
    def generate_report(self):
        print(f"\nReport for {self.get_name()} (Roll No: {self.get_roll_number()})")
        for subject, mark in self.__marks.items():
            print(f"{subject}: {mark}/100")
        print(f"Total Marks: {self.calculate_total()}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")
        print(f"Grade: {self.calculate_grade()}")


# SRP: These classes focus only on their specific role of representing subjects
math = Subject("Math", 100)
science = Subject("Science", 100)
english = Subject("English", 100)
history = Subject("History", 100)

# SRP: Each ReportCard instance is responsible for managing a single student's data
student1 = ReportCard("Alice", 101, [math, science, english])
student2 = ReportCard("Bob", 102, [math, science, history])

# SRP: Handles input of marks for specific students
student1.enter_marks({"Math": 70, "Science": 90, "English": 88})
student2.enter_marks({"Math": 100, "Science": 85, "History": 92})

# LSP & OCP: Abstract method `generate_report` implemented in ReportCard
student1.generate_report()
student2.generate_report()
