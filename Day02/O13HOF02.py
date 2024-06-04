
def callMe():
    print("Apples from Ooty.....")

def fun(fnc):
    print("Hello......")
    fnc()                   # call back
    print("Hi......")
    print("-" * 60)

    def defineMe():
        print("Oranges from kanpur......")

    return defineMe

def funCallback(fnc):
    print("Mera Bharath Mahan.....")
    fnc()
    print("India is great.......")


funCallback(fun(callMe))
