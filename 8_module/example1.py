import time 
import sys
import random
import os
import pymongo


# while True:
#     r=random.randint(100,200)
#     print(r)
#     time.sleep(1)
#     if 180<r<200:
#         print('breaking the loop')
#         sys.exit()

# print('close all position')


ca=os.getcwd()
print(ca)

address=ca+'/8.module/trades.txt'
print(address)
d=open(address,'r')
v=d.read()
print(v)
d.close()