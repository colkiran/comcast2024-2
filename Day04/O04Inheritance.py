
"""
Recap
-----
oops
1. class
2. object
3. isinstance
4. methods
5. __init__()
6. self
7. __dict__
8. class attribute
9. @classmethod
10. cls
11. Operator Overloading - __str__, __eq__, __gt__, __ge__, @total_ordering, __len__, __iter__, append, __add__, __sub__, __mul__, __truediv__, __floordiv__, __set_item__, __get_item__
12. private variable
13. property(), @property
14. @staticmethod
"""

class Animal:
    def __init__(self):
        print("Animal Ctor......")
        self.a = 10

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Fish(Animal):

    def swim(self):
        print("Fishes swim.....")


cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()
print("-" * 60)

print(cuckoo.__dict__)

print("-" * 60)
dolphin = Fish()
dolphin.eat()
dolphin.swim()
print(dolphin.__dict__)
