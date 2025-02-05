import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__), "class"))
from Class.subject import Subject
from Class.report_card import ReportCard


math = Subject("Math", 100)
science = Subject("Science", 100)
english = Subject("English", 100)
history = Subject("History", 100)

#Create students with their subjects
student1 = ReportCard("Alice", 101, [math, science, english])
student2 = ReportCard("Bob", 102, [math, science, history])

#Enter marks for the students
student1.enter_marks({"Math": 70, "Science": 90, "English": 88})
student2.enter_marks({"Math": 100, "Science": 85, "History": 92})

#Generate reports for the students
student1.generate_report()
student2.generate_report()
