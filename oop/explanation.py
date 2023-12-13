# Attributes that is the same across all the instance of the class is called the class attributes and they are declared at the class level above the constructor

class Point:
    color = "blue"

    # the __init__ is a dunda method or magic method. It means the default constructor is no longer in use. We're defining our own constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # the instance variables of the class are declared in the constructor, and they are available throughout the class
    def draw(self):
        print(f"drawing from point {self.a} to point {self.b}")

    def __str__(self):
        return f"Point({self.a}, {self.b})"


the_color = Point.color
print(the_color)
point1 = Point(1, 2)
point2 = Point(5, 6)
point1.draw()
point2.draw()

print(Point.color)
point1.a = 3
point1.b = 7
print(point1)
