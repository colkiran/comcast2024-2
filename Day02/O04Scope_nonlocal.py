
def outerFun():
    gname = "Sachin"
    def innerFun():
        nonlocal gname      # only local variable can be declared as                     nonlocal

        gname = "Mr." + gname
        print("Hello World")
        print(f"Greetings {gname}")

    innerFun()
    print(gname)

outerFun()
