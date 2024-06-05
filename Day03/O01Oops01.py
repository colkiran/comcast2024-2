
class Player:           # pascal casing

    def get_runs(self):
        print("runs scored.....")

sachin = Player()           # calls the default constructor
sachin.get_runs()
print(type(sachin))         # RTTI - runtime type identification

# __main__  - double underscore = dunder_main

print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
