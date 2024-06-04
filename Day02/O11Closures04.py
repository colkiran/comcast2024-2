
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMostFun

    return innerFun

engGrt = outerFun("Welcome")
engGrtTiger = engGrt("tiger")
engGrtTiger("Sheroff")

engGrtTiger = engGrt("lion")
engGrtTiger("Sheroff")

engGrtTiger = engGrt("bear")
engGrtTiger("Sheroff")



"""
engGrt = outerFun("Welcome")
engSngArw = engGrt("------>")
tmlGrt = outerFun("Vanakam")
tmlGrtDblArw = tmlGrt("=======>>")


engSngArw("Sachin")
tmlGrtDblArw("Karthik")
"""