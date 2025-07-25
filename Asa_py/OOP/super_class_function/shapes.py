class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()#optional
        print(f"it is a circle with an area of {3.14 * self.radius ** 2} square cm.")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()  # optional
        print(f"it is a square with an area of {self.width ** 2} square cm.")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()  # optional
        print(f"it is a square with an area of {self.width * self.height / 2} square cm.")

circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("green", True, 7, 8)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")
circle.describe()

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
square.describe()

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
triangle.describe()
