
from abc import ABC, abstractmethod
class Employee(ABC):
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's job....")

class Developer(Employee):

    def doJob(self):
        print("Developer's job....")

mike = Manager()
dave = Developer()

def BankJob(emp):
    print("Bank job started......")
    emp.doJob()
    print("Bank job ended......")
    print("-" * 60)

BankJob(mike)
BankJob(dave)
