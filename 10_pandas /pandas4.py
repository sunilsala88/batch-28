
# import pandas as pd

# df=pd.read_csv('/Users/algotrading2024/batch 28/10_pandas /Unicorn_companies.csv')
# df.set_index('Company',inplace=True)
# # df.set_index('Name',inplace=True)
# # print(df)
# # print(df.loc['Allergan Plc','EPS'])
# # print(df.iloc[4,-1])

# # print(df.loc[['Apple Inc','Abbvie Inc','Abbott Laboratories'],['Price','EPS']])
# # print(df.loc['Apple Inc':'Abbott Laboratories','Price':'EPS'])


# # print(df.iloc[[0,1,2],[-2,-1]])
# # print(df.iloc[0:3,-2:])


# print(df.loc['Klarna':'JUUL Labs','Date Joined':'Continent'])
# print(df.iloc[4:9,1:-2])


# # importing pandas module
# import pandas as pd 
 
# # Define a dictionary containing employee data 
# data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
#          'key1': ['K0', 'K1', 'K0', 'K1'],
#          'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
#         'Age':[27, 24, 22, 32],} 
   
# # Define a dictionary containing employee data 
# data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
#          'key1': ['K0', 'K0', 'K0', 'K0'],
#          'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
#         'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# # Convert the dictionary into DataFrame  
# df = pd.DataFrame(data1)
 
# # Convert the dictionary into DataFrame  
# df1 = pd.DataFrame(data2) 
  
 
# print(df, "\n\n", df1) 

# # merging dataframe using multiple keys
# res1 = pd.merge(df, df1, on='key')
 
# print(res1)


# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'degree': ['Msc', 'MA', 'MCA', 'Phd']}

# Define a dictionary containing employee data
data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=[0, 1, 2, 3])

# # Convert the dictionary into DataFrame
# df1 = pd.DataFrame(data2, index=[16, 5, 6, 7])

# print(df, "\n\n", df1,'\n\n')

# print(pd.concat([df,df1]).reset_index(drop=True))

print(df)

df.rename(columns={'degree':'qualification'},inplace=True)
print(df)