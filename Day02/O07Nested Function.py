
def outerFun(gname):

    def innerFun():
        
        print("Hello World")
        print(f"Gretings {gname}")

    innerFun()

outerFun("Rahul")

