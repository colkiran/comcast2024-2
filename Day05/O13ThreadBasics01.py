"""
GIL = global interpreter lock in python is process lock or a mutex used while dealing with the process

mutex - is a program that prevents multiple threads from accessing the same shared resource simultaneously
"""
import threading
import time

def doJob():
    print(f"Going to sleep for 2 secs - {threading.current_thread().name}")
    time.sleep(2)
    print(f"Just woke up from the sleep - {threading.current_thread().name}")

st = time.perf_counter()

thrd1 = threading.Thread(target=doJob, name="th1")
thrd2 = threading.Thread(target=doJob, name="th2")
thrd3 = threading.Thread(target=doJob, name="th3")

thrd1.start()
thrd2.start()
thrd3.start()

# main thread wait for the child threads
thrd1.join()
thrd2.join()
thrd3.join()


et = time.perf_counter()
print(f"Total time taken to execute {round(et - st, 2)} secs......")

