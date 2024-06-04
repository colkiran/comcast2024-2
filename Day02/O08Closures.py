
def outerFun(gname):

    def innerFun():

        print("Hello World")
        print(f"Gretings {gname}")

    return  innerFun

inref = outerFun("Rahul")

print("sample text\n" * 5)

inref()

print("-" * 60)
outerFun("Sachin")()        # calls the innerfun

