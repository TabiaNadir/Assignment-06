class Engine:
    def start(self):
        print("Engine has started.")


class Car:
    def __init__(self, engine):
        self.engine = engine  
    def start_car(self):
        self.engine.start()  

my_engine = Engine()

my_car = Car(my_engine)

my_car.start_car()
