class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Wheels:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horsepower, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)
        self.wheels = [Wheels(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horsepower}(HP) with {self.wheels[0].size}-inch wheels"

car = Car("Ford", "Mustang", 450, 26)
car2 = Car("Chevrolet", "Camaro", 455, 28)

print(car.display_car())
print(car2.display_car())