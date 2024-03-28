class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

    def show(self):
        print("Name: ", self.name)

    def type(self):
        pass

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Woof")

    def type(self):
        print("Type: Dog")
        print("Color: ", self.color)

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Meow")

    def type(self):
        print("Type: Cat")
        print("Color: ", self.color)

class Parrot(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Car")

    def type(self):
        print("Type: Parrot")
        print("Color: ", self.color)

class Hamster(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("eeeeee")

    def type(self):
        print("Type: Hamster")
        print("Color: ", self.color)

dog = Dog("Oscar", "Black")
dog.show()
dog.type()
dog.sound()
print()

cat = Cat("Felix", "Black-white")
cat.show()
cat.type()
cat.sound()
print()

parrot = Parrot("Kesha", "REd")
parrot.show()
parrot.type()
parrot.sound()
print()

hamster = Hamster("Lux", "Brown")
hamster.show()
hamster.type()
hamster.sound()
