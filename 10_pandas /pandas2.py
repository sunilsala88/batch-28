import numpy as np
import pandas as pd

np1=np.arange(100,125).reshape(5,5)
print(np1)

pd1=pd.DataFrame(np1)
print(pd1)

a=np1[0,0]

print(a)

d1={'name':['amzn','tsla','goog'],'prices':[5666,899,300]}
df1=pd.DataFrame(d1,index=['a','b','c'])
print(df1)

n=[[1,2,3],[5,6,7]]
df2=pd.DataFrame(n,index=['r1','r2'],columns=['c1','c2','c3'])
print(df2)