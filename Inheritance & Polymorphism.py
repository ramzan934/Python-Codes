
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")

    def stop(self):
        print(f"{self.brand} vehicle stopped.")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def info(self):
        print(f"Car: {self.brand} {self.model}")


class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def info(self):
        print(f"Bike: {self.brand}")


class ElectricCar(Car):
    def start(self):
        print(f"{self.brand} {self.model} electric system started.")


# Objects
car = Car("Toyota", "Corolla")
bike = Bike("Yamaha")
ev = ElectricCar("Tesla", "Model S")

# Car
car.info()
car.start()
car.stop()

# Bike
bike.info()
bike.start()
bike.stop()

# Electric Car (Method Overriding)
ev.info()
ev.start()

