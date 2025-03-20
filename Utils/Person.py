class Student:
    def __init__(self, age, name):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"
    
if __name__ == "__main__":
    student = Student("Maks", 20)
    print(student)