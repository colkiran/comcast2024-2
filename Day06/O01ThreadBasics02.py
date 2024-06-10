import threading
import time

def doJob(secs, tname):
    print(f"Going to sleep for 2 secs.....{tname}-> {threading.current_thread().name}")
    time.sleep(secs)
    print(f"Just woke up ....{tname} -> {threading.current_thread().name}")

threads = []
st = time.perf_counter()

for i in range(500):
    t = threading.Thread(target=doJob, name="th" + str(i), args=[2, "thrd"+str(i)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

et = time.perf_counter()
print(f"The total time taken is  :{round(et - st, 2)}")