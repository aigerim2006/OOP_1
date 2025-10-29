class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    def description(self):
        return f"{self.brand}{self.model} travels at speed {self.speed} km/hour"
    def acceleration(self, amount):
        self.speed += amount
        print(f"{self.brand}{self.model} accelerated by {amount} km/hour")

toyota = Car("Toyote", "Corolla", 120)
bmw = Car("BMW", "X7", 100)
print(toyota.description())
toyota.acceleration(40)
print(toyota.description())
print(bmw.description())
bmw.acceleration(20)
print(bmw.description())
