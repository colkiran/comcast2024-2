
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2EE', 'spring', 'hibernate', 'AngualarJS', 'ReactJS']


    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)


emp1 = Employee("Austin", 45000)
print(emp1)
print("-" * 60)

print(len(emp1))

print("-" * 60)

# list comprehension
print([emp for emp in emp1])
