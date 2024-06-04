
def outerFun(greet, flag):

    def innerFun1(gname):
        print(greet, gname)

    def innerFun2(gname):
        print(greet, gname)

    if flag == 1:
        return innerFun1
    else:
        return innerFun2

inRef = outerFun("Welcome", 1)
inRef("Rahul")

inRef = outerFun("Hola", 2)
inRef("Messi")

outerFun("Vanakam", 1)("Krish Srikant")