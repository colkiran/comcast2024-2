
import concurrent.futures
import threading
import time

def doJob(secs):
    print(f"Going to sleep for {secs} seconds.... {threading.current_thread().name}")
    time.sleep(secs)
    print(f"Just woke up......{threading.current_thread().name}")

st = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    thrd1 = executor.submit(doJob, 2)
    thrd2 = executor.submit(doJob, 2)
    thrd3 = executor.submit(doJob, 2)

    thrd1.result()
    thrd2.result()
    thrd3.result()

et = time.perf_counter()
print(f"Total time taken is {round(et - st, 2)}")


