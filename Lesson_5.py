from termcolor import cprint
from random import randint as Generate_Number 
from Utils.Calculator import division
from Utils.Person import Student
from decouple import config
MyFr = Student(20, "Kevin")
cprint("Hi", "green")

print(config("DATABASE_URL"))

commented = config("COMMENTED", default=0)
print(commented * 2)