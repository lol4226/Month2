from random import randint

class Figure:
    unit = "cm"
    def __init__(self):
        pass

    def Calculate_Area():
        pass
    
    def Info():
        pass

class Square(Figure):
    def __init__(self, side_Lenght):
        self.__side_Lenght = side_Lenght
    
    def Calculate_Area(self) -> int:
        return self.__side_Lenght**2

    def Info(self):
        print(f"Square side lenght: {self.__side_Lenght} cm, area: {self.Calculate_Area()} cm")

class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def Calculate_Area(self) -> int:
        return self.__length * self.__width
    
    def Info(self):
        print(f"Rectangle length: {self.__length} cm, width: {self.__width} cm, area: {self.Calculate_Area()} cm")

def Create_Random_Squares_And_Rectangled(Squares: int, Rectangles: int) -> list:
    Figures = []
    for i in range(Rectangles):
        rectangle = Rectangle(randint(2, 20), randint(2, 20))
        Figures.append(rectangle)
    for i in range(Squares):
        square = Square(randint(2, 13))
        Figures.append(square)
    return Figures

Figures = Create_Random_Squares_And_Rectangled(2, 3)

for figure in Figures:
    figure.Info()