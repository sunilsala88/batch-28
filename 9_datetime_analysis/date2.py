# import datetime
import datetime as dt
#from datetime import *


d2=dt.datetime(2024,11,11,20,35,2)
print(d2)

t1=dt.timedelta(minutes=1)
print(t1)

print(d2+t1)

print(d2.weekday())
# 0->Mon
#1->tue