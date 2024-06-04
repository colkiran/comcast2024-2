
def BankFun(fnc):

    def helperFun(arg):
        print("logging into the server.....")
        fnc(arg)
        print("Logging out of the server.....")
        print("-" * 60)

    return helperFun

@BankFun            # deposit = BankFun(deposit)
def deposit(amt):
    print(f"amount {amt} deposited into the account ending ######.##......")

@BankFun
def withDraw(amt):
    print(f"amount {amt} debited from the account ending ####")

deposit(50000)
withDraw(19500)

# time taken by the function to execute



