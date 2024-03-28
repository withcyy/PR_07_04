class Employer:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "Tis is Emloyeer class"

    def __int__(self):
        return self.age

class President(Employer):
    def __init__(self, age):
        super().__init__(age)

    def __str__(self):
        return "This is President calss"

    def __int__(self):
        return self.age

class Manageer(Employer):
    def __init__(self, age):
        super().__init__(age)

    def __str__(self):
        return "This is Manageer class"

    def __int__(self):
        return self.age

class Worker(Employer):
    def __init__(self, age):
        super().__init__(age)

    def __str__(self):
        return "This is Worker class"

    def __int__(self):
        return self.age

employer = Employer(50)
print(str(employer))
print(int(employer))

president = President(60)
print(str(president))
print(int(president))

worker = Worker(20)
print(str(worker))
print(int(worker))

manageer = Manageer(30)
print(str(manageer))
print(int(manageer))