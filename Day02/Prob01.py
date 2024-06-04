
import time

def timeCalc(fnc):

    def helper(arg):
        print("Executing function......")
        st = time.perf_counter()
        fnc(arg)
        et = time.perf_counter()
        print("Completed execution......")
        print(f"Time taken by the function to execute {round(et - st, 2)}")
        print("-" * 60)

    return helper


@timeCalc
def fun(x):
    lst = []
    for i in range(1, x):
        for j in range(1, i+1):
            lst.append(j ** 2)

fun(6500)

"""
import time

st = time.perfcounter()
"""