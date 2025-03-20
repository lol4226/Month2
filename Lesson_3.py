from xml.sax.handler import property_xml_string


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    def __str__(self):
        return f"Name: {self.__name}, age: {self.__age}"

class Car:
    def __init__(self, model, year, color, speed, owner):
        self.__model = model
        self.__year = year
        self.__color = color
        self.__speed = speed
        self.__owner = None
    
    @property
    def model(self):
        return self.__model
    
    @property
    def year(self):
        return self.__year
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        if type(color) == str:
            self.__color = color
        else:
            raise TypeError("Wrong type of color, need str")
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, own):
        if type(own) == Person:
            self.__owner = own
    
    def __str__(self):
        return f"Model: {self.__model}, date of create: {self.__year}, color: {self.__color}, speed: {self.__speed}"
    
    def Drive(self):
        print(f"Car: {self.__model} driving")

    def __lt__(self, other):
        return self.year < other.year
    
    def __gt__(self, other):
        return self.year > other.year
    
    def __eq__(self, other):
        return self.year == other.year
    
    def __ne__(self, other):
        return self.year == other.year
    
    def __gt__(self, other):
        return self.year <= other.year
    
    def __gt__(self, other):
        return self.year >= other.year

class FuelCar(Car):
    __totalFuel = 0

    @classmethod
    def BuyFuel(cls, amount):
        cls.__totalFuel += abs(amount)

    @staticmethod
    def GetFuelType():
        return "Ai 95 fuel"

    def __init__(self, model, year, color, speed, fuel_Bank, owner = None):
        # super().__init__(model, year, color, speed)
        Car.__init__(self, model, year, color, speed, owner)
        self.__fuel_Bank = fuel_Bank
        FuelCar.__totalFuel -= self.__fuel_Bank
    
    @property
    def fuel_Bank(self):
        return self.__fuel_Bank
    
    def Drive(self):
        return super().Drive() + " by fuel"
    
    def __str__(self):
        return super().__str__() + f", fuel bank: {self.fuel_Bank}"

    def __add__(self, other):
        return self.__fuel_Bank + other.__fuel_Bank
    
    @classmethod
    def Print_Fuel_Amount(cls):
        print(f"Fuel Amount: {cls.__totalFuel}, litters of fuel: {cls.GetFuelType()}")

class ElectricCar(Car):
    def __init__(self, model, year, color, speed, battery, owner = None):
        super().__init__(model, year, color, speed, owner)
        self.__battery = battery
    
    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        if type(value) == int:
            self.__battery = value
        else:
            raise TypeError("Wrong type of battery value, need int")

    def __str__(self):
        return super().__str__() + f", battery value: {self.__battery}"

    def Drive(self):
        return f"Car: {self.model} driving by battery"
    
class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color, speed, fuel_Bank, battery, owner = None):
        FuelCar.__init__(self, model, year, color, speed, fuel_Bank, owner)
        ElectricCar.__init__(self, model, year, color, speed, battery, owner)
        # self.battery = battery
    


# car = Car("Nissan GTR", 2002, "Red", 250)
# print(car)

MyFriend = Person("Alihan", 20)

FuelCar.BuyFuel(500)
fuelCar = FuelCar("Toyota Supra", 2009, "Blue", 200, 70)
print(fuelCar)
fuelCar.owner = MyFriend

tesla = ElectricCar("Tesla Model x", 2020, "White", 260, 20000)
print(tesla)
tesla.owner = MyFriend

chevrolet = HybridCar("Chevrolet Volt", 2009, "Red", 200, 80, 9500)
print(chevrolet)
print(chevrolet.Drive())
print(HybridCar.mro())
chevrolet.owner = Person("Jim", 22)

number_one, number_two = 20, 9
print(f"number one is greater than number two: {number_one > number_two}")
print(f"Toyota is less than chevrolet: {fuelCar < chevrolet}")

print(chevrolet + fuelCar)
print(chevrolet.owner.name)
FuelCar.Print_Fuel_Amount()
    
