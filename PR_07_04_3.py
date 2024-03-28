class Employer:
    def Print(self):
        print("This is Employer class")

class President(Employer):
    def Print(self):
        print("This is President class")

class Manageer(Employer):
    def Print(self):
        print("This is Manager class")

class Worker(Employer):
    def Print(self):
        print("Tis is Worker class")

employer = Employer()
employer.Print()

president = President()
president.Print()

manageer = Manageer()
manageer.Print()

worker = Worker()
worker.Print()