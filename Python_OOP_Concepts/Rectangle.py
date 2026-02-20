class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def calculate_area(self):
        area = self.length * self.breadth
        print(f"Area of Rectangle: {area}")
        return area
    def update_dimensions(self, new_length, new_breadth):
        if new_length > 0 and new_breadth > 0:
            self.length = new_length
            self.breadth = new_breadth
        else:
            print("Length and breadth must be positive values.")

l = int(input("Enter Length : "))
b = int(input("Enter Breadth : "))
rectangle1 = Rectangle(l,b)
rectangle1.calculate_area()

new_l = int(input("Enter New Length : "))
new_b = int(input("Enter New Breadth : "))
rectangle1.update_dimensions(new_l , new_b)
rectangle1.calculate_area() 