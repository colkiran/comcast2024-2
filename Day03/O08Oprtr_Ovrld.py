
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # it also works for != (not equal to)
    def __eq__(self, other):
        return self.salary == other.salary

    # it works for less than also
    def __gt__(self, other):
        return self.salary > other.salary



emp1 = Employee("Slater", 45000)
print(emp1)

print("-" * 60)
emp2 = Employee("Kevin", 50000)
print(emp2)

print("-" * 60)
# it is comparing the addresses by default
# we will make it compare the salaries

if emp1 != emp2:
    print("{}'s salary {} is NOT equal to {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary {} is equal to {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

if emp1 < emp2:
    print("{}'s salary {} is less than {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary {} is greater than {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

print(emp1 <= emp2)
