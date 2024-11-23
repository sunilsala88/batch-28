import pandas as pd
df=pd.read_csv('/Users/algotrading2024/batch 28/10_pandas /sp500.csv')

# df.dropna(axis=0,inplace=True)
# df['EPS']=df['EPS'].astype(int)

# df.drop('Price',axis=1,inplace=True)
# df.drop_duplicates('Sector',inplace=True)
print(df)

# print(df.shape)
# list1=df['Sector'].to_list()
# print(list1)
# #group_by
s='Information Technology'


new_df=df[df['Sector']==s].fillna(method='ffill',axis=0)
print(new_df)
