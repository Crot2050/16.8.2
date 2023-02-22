class Rectangel:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle(self):
        return 3.14 * self.r ** 2
    
rect1 = Rectangel(2, 4)
rect2 = Rectangel(4, 6)
print(rect1.get_area(),
      rect2.get_area())

square1 = Square(5)
square2 = Square(6)
print(square1.get_area_square(),
      square2.get_area_square())

circle1 = Circle(7)
circle2 = Circle(8)
print(circle1.get_circle(),
      circle2.get_circle())

figures = (rect1, rect2, square1, square2, circle1, circle2)
for figure in figures:
    if isinstance(figure, Square):
        print("Площадь квадрата = ", figure.get_area_square())
    elif isinstance(figure, Circle):
        print("Площадь круга = ", figure.get_circle())
    else:
        print("Площадь прямоугольника = ", figure.get_area())

