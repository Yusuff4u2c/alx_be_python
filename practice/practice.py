class Car:
    def __init__(self, make):
        self.make = make

    def intro(self):
        return f"This car is a {self.make}."
    
class Jeep(Car):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model
    def start(self):
        print(f"The {self.make} {self.model} is starting.")

myCar = Jeep("Jeep", "Wrangler")

