#yahoo finance
#yfinance==0.2.37
import yfinance as yf
import pandas as pd
# data=yf.download(tickers='^NSEI',period='1y')
# print(data)

#10y nifty
#10 y banknifty data
nifty=yf.download(tickers='^NSEI',period='1y')

print(nifty.info())
print(nifty)
# nifty.drop('Ticker',axis=0,inplace=True)



# bnifty=yf.download(tickers='^NSEBANK',period='1y')
# bnifty.drop('Ticker',axis=0,inplace=True)
# print(bnifty)

# df=pd.merge(nifty,bnifty,on='Date')

# print(df)

# df1=pd.concat([nifty,bnifty])
# print(df1)



# nifty=yf.download(tickers='BTC',period='1d',interval='1m')
# print(nifty)
# print(nifty.info())

nifty=yf.download(tickers='TSLA',interval='30m',start='2024-10-25',end='2024-11-30')
print(nifty)
print(nifty.info())
