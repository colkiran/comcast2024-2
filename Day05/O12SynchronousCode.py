import time

def fun():
    print("Function going to sleep.....")
    time.sleep(2)
    print("Function just woke up.......")
    print("-" * 60)

st = time.perf_counter()

fun()
fun()
fun()

et = time.perf_counter()
print(f"total time taken by the code to execute {round(et- st, 2)}......")
