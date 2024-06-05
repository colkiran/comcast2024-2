
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary


emp1 = Employee("Ben", 8000)
print(emp1)

print("-" * 60)

emp2 = Employee("Jack", 4000)
print(emp2)
print("-" * 60)

print(f"Addition emp1 + emp2 :{emp1 + emp2}")

print("-" * 60)

print(f"Subtraction emp1 - emp2 :{emp1 - emp2}")

print("-" * 60)

print(f"Multiplication emp1 * emp2 :{emp1 * emp2}")

print("-" * 60)

print(f"Division emp1 / emp2 :{emp1 / emp2}")

print("-" * 60)

print(f"True Division emp1 // emp2 :{emp1 // emp2}")
