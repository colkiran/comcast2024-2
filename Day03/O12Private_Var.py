
class Employee:

    def __init__(self, name):
        self.__name = name          # private variable
        self.tech = ['C++', 'Java', 'J2EE', 'spring', 'hibernate', 'AngualarJS', 'ReactJS']

    def __str__(self):
        return self.__name + " - " + ", ".join([str(v) for v in self.tech])

print("-" * 60)

emp1 = Employee("Tom")
print(emp1)

print("-" * 60)

print(emp1.__dict__)
# emp1.__name = "Jack"
# print(emp1._Employee__name)

print("-" * 60)

emp1._Employee__name = "Jack"
print(emp1)

