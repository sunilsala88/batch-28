
import pandas as pd
df = pd.read_csv("/Users/algotrading2024/batch 28/10_pandas /stock_value.csv")
print(df)

date1=pd.to_datetime('2023-01-01')
delta1=pd.Timedelta(days=1)
print(date1)
print(delta1)
print(date1+delta1)

df['Date']=pd.to_datetime(df['Date'])
print(df)
df['year']=df['Date'].dt.day_name()
print(df)