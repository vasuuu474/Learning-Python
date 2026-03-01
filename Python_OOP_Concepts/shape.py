from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def draw(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def draw(self):
        print("Drawing a Circle")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def draw(self):
        print("Drawing a Rectangle")
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def draw(self):
        print("Drawing a Triangle")
circle = Circle(7)
rectangle = Rectangle(10, 5)
triangle = Triangle(8, 6) 
print("Circle Area:", circle.area())
circle.draw()
print("\nRectangle Area:", rectangle.area())
rectangle.draw()
print("\nTriangle Area:", triangle.area())
triangle.draw()