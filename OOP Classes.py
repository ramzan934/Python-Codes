
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} started.")
        else:
            print("Car is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} stopped.")
        else:
            print("Car is already stopped.")

    def status(self):
        if self.is_running:
            print(f"{self.brand} {self.model} is running.")
        else:
            print(f"{self.brand} {self.model} is not running.")


# Object Creation
my_car = Car("Honda", "Civic")

# Checking Status
my_car.status()

# Starting Car
my_car.start()
my_car.status()

# Stopping Car
my_car.stop()
my_car.status()

# Trying Multiple Actions
my_car.start()
my_car.start()  # Already running message

my_car.stop()
my_car.stop()   # Already stopped message
