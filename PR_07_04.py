class Wheels:
    def __init__(self, count):
        self.count = count

    def rotate(self):
        print("Wheels are rotating.")


class Engine:
    def __init__(self, power):
        self.power = power

    def work(self):
       print("Engine works")


class Doors:
    def __init__(self, count):
        self.count = count

    def open(self):
        print("Doors opened.")

    def close(self):
        print("Doors closed.")


class Car(Wheels, Engine, Doors):
    def __init__(self, wheels_count, engine_power, doors_count):
        Wheels.__init__(self, wheels_count)
        Engine.__init__(self, engine_power)
        Doors.__init__(self, doors_count)

    def work(self):
        super().work()
        print("Car works")

car = Car(wheels_count=4, engine_power=200, doors_count=4)
car.work()
car.rotate()
car.open()
car.close()
