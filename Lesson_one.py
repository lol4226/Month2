class Transport:
    def __init__(self, Model: str, year: int, color: str, speed: int):
        self.model = Model.capitalize()
        self.year = year
        self.color = color.capitalize()
        self.speed = speed

    def Change_Color(self, Color: str):
        print(f"{self.model.capitalize()} change to color: {Color}")
        self.color = Color.capitalize()

class Plane(Transport):
    # constructor matching
    def __init__(self, Model, year, color, speed):
        super().__init__(Model, year, color, speed)
    
class Car(Transport):
    counter = 0

    def __init__(self, model: str, year: int, color: str, speed: int, penalties = 0):
        # attributes
        super().__init__(model, year, color, speed)
        self.penalties = penalties
        Car.counter += round(2 / 2)
    
    def Drive(self, city):
        print(f"car: {self.model} is driving to city: {city}")
    
    def Signal(self, NumberOfTimes, Sound):
        for i in range(NumberOfTimes):
            print(f"Car: {self.model}, is signalling: {Sound}")

class Truck(Car):
    counter = 0
    def __init__(self, Model, year, color, speed, penalties = 0, load_capacity = 0):
        super().__init__(Model, year, color, speed, penalties)
        self.load_capacity = load_capacity
        Truck.counter += round(2 / 2)

    def load_cargo(self, weight, product_type):
        if weight > self.load_capacity:
            print(f"dont load cargo to Truck")
        else:
            print(f"Success to load cargo of {product_type} {weight} kilo")

print("Start")
print(f"Factory Car Produce: {Car.counter}")
number = 5
BMW = Car("BMW X7", 20, "Red", 200)
print(BMW)
print(f"Model: {BMW.model}, year: {BMW.year} color: {BMW.color}, speed: {BMW.speed}, penalties: {BMW.penalties}")
Honda = Car("Honda fit", 2009, "Red", 200, 500)
Honda.color = "yeallow".capitalize()
print("New color: " + Honda.color)
Honda.Drive("Tokyo")
BMW.Drive("USA")
Honda.Change_Color("Blue")
BMW.Signal( 50, "Beeeep")
print(f"Car Counter: {Car.counter}")

boeing = Plane("boeing 777", 2022, "White", 900)
print(f"Model: {boeing.model}, year: {boeing.year}, color: {boeing.color}, speed: {boeing.speed}")
boeing.Change_Color("Black")

Daf = Truck("Daf 205", 2000, "red", 200, 900, 20000)
Daf.Change_Color("Blue")
Daf.load_cargo(50000, "Potatoes")
print(f"Factory Truck produced: {Truck.counter} trucks")

marks = {"Russia": [5, 3, 2, 5]}

for mark in marks:
    marks["Russia"].
    for m in marks[mark]:
        print(m)