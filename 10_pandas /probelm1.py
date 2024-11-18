# import pandas as pd

# data=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')

# # print(data)
# df1=data[1]
# # print(df1)
# data=pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')

# # print(data)
# df2=data[2]
# df2=df2[['Company','Symbol','Date added']]
# print(df2)

# df1.rename(columns={"Company name":'Company',"Date added[16]":"Date added"},inplace=True)
# df1=df1[['Company','Symbol','Date added']]
# print(df1)
# df3=pd.concat([df1,df2]).reset_index(drop=True)
# print(df3)


import pandas as pd

data=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')

# print(data)
df1=data[7]

data=pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')
df1.set_index('Year',inplace=True)
df1=df1.loc[2001:2020,:]
print(df1)

# print(data)
df2=data[3]
df2.set_index('Year',inplace=True)
df2=df2.loc[2001:2020,:]
print(df2)

df3=pd.merge(df1,df2,on='Year')
print(df3)

# df2=df2[['Company','Symbol','Date added']]
# print(df2)

# df1.rename(columns={"Company name":'Company',"Date added[16]":"Date added"},inplace=True)
# df1=df1[['Company','Symbol','Date added']]
# print(df1)
# df3=pd.concat([df1,df2]).reset_index(drop=True)
# print(df3)