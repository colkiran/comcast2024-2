
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1= Player("Sehwag", 30)
ply1.get_details()

print("-" * 60)
ply2 = Player("Yuvraj", 28)
ply2.get_details()

print("-" * 60)
# self will have the name of an object that made a call to the function

ply2.runs = 250
print("Ply2 :", ply2.__dict__)

print("Ply1 :", ply1.__dict__)