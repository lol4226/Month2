from random import randint, choice

class Person:
    def __init__(self, full_Name: str, age: int, is_Married: bool):
        self.full_Name = full_Name
        self.age = age
        self.is_Married = is_Married
    
    def Introduce_Myself(self):
        print(f"FullName: {self.full_Name}, age: {self.age}, married: {self.is_Married}")

class Student(Person):
    def __init__(self, full_Name, age, is_Married, marks: dict):
        super().__init__(full_Name, age, is_Married)
        self.marks = marks

    def GetAverageScoreOfAllLessons(self):
        for Lesson in self.marks:
            count = 0
            for mark in self.marks.get(Lesson):
                count += mark
            result = count / len(self.marks.get(Lesson))
            print(f"Lesson: {Lesson}, Average score: {result}")

class Teacher(Person):
    base_Salary = 30000
    def __init__(self, full_Name, age, is_Married, experience):
        super().__init__(full_Name, age, is_Married)
        self.experience = experience

    def CalculateBaseSalary(self) -> print:
        for i in range(4, self.experience):
            self.base_Salary += self.base_Salary / 100 * 5
        print(f"Teacher base_salary: {round(self.base_Salary)}")

def Create_Students() -> list:
    names = ["Egor", "Alihan", "Sanya", "Andrey"]
    students = []
    for i in range(3):
        student = Student(choice(names), randint(20, 30), choice([True, False]), {
                  "Russia": [randint(2, 5) for i in range(5) ],
                  "English": [randint(2, 5) for i in range(5)]})
        students.append(student)
    return students

teacher = Teacher("Marina Petrovovna", 35, True, 9)
teacher.Introduce_Myself()
teacher.CalculateBaseSalary()

students = Create_Students()
for student in students:
    student.Introduce_Myself()
    student.GetAverageScoreOfAllLessons()

