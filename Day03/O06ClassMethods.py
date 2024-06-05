
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player initialized.....")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fnm, lnm, age):
        print("factory....")
        # calls the player constructor
        return cls(f"{fnm} {lnm}", age)


ply1 = Player("Virat Kholi", 34)
ply1.get_details()

print("-" * 60)
# accept name in format of - firstname and lastname
ply2 = Player.CreatePlayer("Rohit", "Sharma", 35)
ply2.get_details()





