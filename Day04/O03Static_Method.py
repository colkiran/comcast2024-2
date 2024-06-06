
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    @staticmethod
    def Pro_fund(amt):
        return amt * 0.05


emp1 = Employee("Micheal", 60000)
print(emp1)

print(f"Provident Fund Deduction  - {Employee.Pro_fund(emp1.salary)}")