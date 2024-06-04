
def sum(x, y):
    print("Sum function called...")
    return x + y

def diff(x, y):
    print("Diff function called....")
    return x - y

def outerFun(fnc):
    loginfo = "Logging into the service......"
    def helper(*args):
        print(loginfo)
        print(fnc(*args))
        print("-" * 60)

    return helper


sumlogger = outerFun(sum)
sumlogger(38, 86)

difflogger = outerFun(diff)
difflogger(86, 29)
