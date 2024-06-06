
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def getBalance(self):
        pass

    def withdraw(self):
        pass

class Savings(Account):

    def getBalance(self):
        print("Balance in the account ending #### is ######.##")
    def deposit(self):
        print("Amount credited into the account.....")

sav1 = Savings()
sav1.getBalance()
sav1.deposit()

print("-" * 60)
class CurrentAccount(Account):

    def getBalance(self):
        print("Balance in the account ending #### is ######.##")

cur1 = CurrentAccount()
cur1.getBalance()