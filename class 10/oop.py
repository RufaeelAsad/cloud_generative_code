class University:
    def __init__(self, uniname):
        self.cUniNmae = uniname

class Student(University):
    def __init__(self, studentName):
        super().__init__('Air Universtiy Islamabad')
        self.cStudentName = studentName

firstStudent = Student('Rufaeel');

print(f"Student {firstStudent.cStudentName}")
print(f"Universtiy {firstStudent.cUniNmae}")

