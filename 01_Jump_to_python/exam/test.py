import time
from datetime import datetime

sdt = datetime.now()
time.sleep(1)
edt = datetime.now()

adt =  edt -sdt
print(adt)
adt = str(adt)
s = float(adt[5:15])
m = int(adt[2:4])
print(m,s)
print(type(s))

