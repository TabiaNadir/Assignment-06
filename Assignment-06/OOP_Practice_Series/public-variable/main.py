class Car:

    brand = ""
    def start(self):
        print(f"The {self.brand} car is starting...")
        
my_car = Car()
my_car.brand = "Toyota"
my_car.start()
