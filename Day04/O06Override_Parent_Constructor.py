
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = '1 yr'

    def eat(self):
        print("Animals eat.....")


class Bird(Animal):

    # override the parent class constructor
    def __init__(self):
        super().__init__()
        print("Bird Ctor.....")
        self.weight = '1k'

    def fly(self):
        print("Birds fly......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)
print(cuckoo.__dict__)