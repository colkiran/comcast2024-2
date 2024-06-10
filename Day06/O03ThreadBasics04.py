
import time
import threading
import concurrent.futures

def doJob(secs):
    print(f"Going to sleep for {secs} seconds.... {threading.current_thread().name}")
    time.sleep(secs)
    print(f"Just woke up......{threading.current_thread().name}")

st = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [6, 5, 4, 3, 2, 1]
    result = [executor.submit(doJob, sec) for sec in secs]

    for res in result:
        res.result()

et = time.perf_counter()
print(f"The total time taken is {round(et - st , 2)}")
