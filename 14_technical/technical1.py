import yfinance as yf
import pandas as pd
import pandas_ta as ta
import mplfinance as mpf

# import talib
# print(talib.SMA(data['Close'],20))
# print(talib.get_functions())

data=yf.download(tickers='^NSEI',period='1y')
print(data)


# sma20=ta.sma(data['Close'],20)
# ema10=ta.ema(data['Open'],10)



# a=mpf.make_addplot(sma20,color='blue')
# b=mpf.make_addplot(ema10,color='black')
# mpf.plot(data,addplot=[a,b],type='candle',style='yahoo')

#macd
f=25
s=10

macd1=ta.macd(data['Close'],fast=s,slow=f)
print(macd1)

a=mpf.make_addplot(macd1[f'MACD_{s}_{f}_9'],color='blue',panel=1)
b=mpf.make_addplot(macd1[f'MACDh_{s}_{f}_9'],color='black',panel=1,type='bar')
c=mpf.make_addplot(macd1[f'MACDs_{s}_{f}_9'],color='red',panel=1)
mpf.plot(data,addplot=[a,b,c],type='candle',style='yahoo')