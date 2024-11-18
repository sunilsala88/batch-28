# import pandas as pd

# df=pd.read_csv('/Users/algotrading2024/batch 28/10_pandas /Unicorn_companies.csv')
# print(df)

# # print(df['Company'][1073])
# # # print(df.City)

# # print(df[(df['Year Founded']>2015) & (df['Country']=='China')])

# print(df.set_index('Company'))

import pandas as pd
data=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')
df=data[7]
df.to_csv('data.csv')

df1=pd.read_csv('data.csv')

print(df1)
print(df1.info())
df['new']=df1.iloc[:,-1].str.replace('−','-').astype(float)
print(df)
print(df[df['new']<0])
# for i in df1.iloc[:,-1].values:
#     print(i.replace('.',"").replace('−',"-",''))