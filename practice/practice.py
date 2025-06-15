class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self,check):
        return f"The {self.year} {self.make} {self.model} {check} is starting."

    def stop(self):
        return f"The {self.year} {self.make} {self.model} is stopping."

    def honk(self):
        return "Beep beep!"
    
myCar = Car("Toyota", "Corolla", 2020)
print(myCar.start("Yes"))

try:
    print(2/0)
except Exception as e:
    print(f"An error occurred: {e}")