

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

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, indx):
        return self.tech[indx]

    def __setitem__(self, indx, val):
        self.tech[indx] = val

emp1 = Employee("Kenith", 65000)
print(emp1)

print("-" * 60)

print([emp for emp in emp1])

print("-" * 60)
# add python into the list

emp1.append("Python")

print([emp for emp in emp1])

print("-" * 60)

tech = emp1[4]
print(tech)

print("-" * 60)

emp1[2] = "JSP"
print([emp for emp in emp1])

