
gstname = "Sachin Tendulkar"

sports = ['cricket', 'football', 'tennis', 'badmiton', 'basketball', 'swimming']

runs = {'test': 23450, 'odi': 19300, 't20': 3500}

def greet(gst):
    print(f"Greetings {gst}, Welcome to the event.....")


class Employee:

    def __init__(self, name, salary):
        self.name =name
        self.salary =salary


    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

print(f"Module Name :{__name__}")

if __name__ == '__main__':
    greet("Rahul Dravid")

    print("-" * 60)
    emp1 = Employee("Tom", 75000)
    print(emp1)
