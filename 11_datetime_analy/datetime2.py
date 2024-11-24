
import pandas as pd

data=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')

# print(data)
df1=data[1]
# print(df1)
# data=pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')

# # print(data)
# df2=data[2]
# df2=df2[['Company','Symbol','Date added']]
# print(df2)

df1.rename(columns={"Company name":'Company',"Date added[16]":"Date added"},inplace=True)
df1=df1[['Company','Symbol','Date added']]
print(df1)


# print(df2.info())
# s1='2024-01-01'
# a=pd.to_datetime(s1)
# print(a)
# df2['Date added']=pd.to_datetime(df2['Date added'])
# print(df2.info())

list1=[]
for d in df1['Date added']:
    # print(d)
    if d[-3]=='[':
        list1.append(d[:-3])
    else:
        list1.append(d)
df1['Date added']=list1
print(df1)

df1['Date added']=pd.to_datetime(df1['Date added'],format='%d %B %Y')
print(df1)
