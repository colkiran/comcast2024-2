
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.a = 10

    def eat(self):
        print("Animals eat.....")

    def fun(self):
        print("Animal class fun method")

class Person:

    def __init__(self):
        print("Person Ctor.....")
        self.p = 20

    def talk(self):
        print("Person talks....")

    def fun(self):
        print("Person class fun method.....")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()          # calls the parent class Ctor
        Person.__init__(self)
        print("Girl Ctor......")
        self.g = 30

    def walk(self):
        print("Girl Walks.....")


gracy = Girl()
gracy.eat()
gracy.talk()
gracy.walk()

gracy.fun()     # which fun method and why

print("-" * 60)
print(gracy.__dict__)
