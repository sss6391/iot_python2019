import time
import threading
from datetime import datetime

s_dt = datetime.now()
print(s_dt)
def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

print("End")
e_dt = datetime.now()
print(e_dt)
print(e_dt-s_dt)
