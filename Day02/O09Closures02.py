# HOF - higher order function

def outerFun(greet):

    def innerFun(gname):

        print(greet, gname)

    return innerFun

outerFun("Welcome")("Sachin")

# simple curry
print("-" * 60)
engGrt = outerFun("Welcome")
kanGrt = outerFun("Namaskara")
tmlGrt = outerFun("Vanakam")

engGrt("Sachin")
kanGrt("Rahul")
tmlGrt("Ashwin")
