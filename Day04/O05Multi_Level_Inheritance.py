
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.A = 10

    def eat(self):
        print("animals eat")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

        
class Chicken(Bird):

    def msg(self):
        print("Chickens are breeded for consumption....")

    def fly(self):
        print("Chickens seldom fly.....")


chick = Chicken()
chick.eat()
chick.fly()
chick.msg()
