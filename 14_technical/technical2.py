import yfinance as yf
import pandas as pd
import pandas_ta as ta
import mplfinance as mpf



data=yf.download(tickers='TSLA',period='2y')
print(data)
# rsi1=ta.rsi(data['Close'],10)
# print(rsi1)


# a=mpf.make_addplot(rsi1,color='blue',panel=1)
# mpf.plot(data,addplot=[a],type='candle',style='yahoo')

#adx

# adx1=ta.adx(data['High'],data['Low'],data['Close'])['ADX_14']
# print(adx1)

# a=mpf.make_addplot(adx1,color='blue',panel=1)
# mpf.plot(data,addplot=[a],type='candle',style='yahoo')

#supertrend
super=ta.supertrend(data['High'],data['Low'],data['Close'],length=10)
print(super.tail(50))
# a=mpf.make_addplot(super['SUPERTl_10_3.0'],color='blue')
# b=mpf.make_addplot(super['SUPERTs_10_3.0'],color='red')
# mpf.plot(data,addplot=[a,b],type='candle',style='yahoo')

#bollinger band
bands=ta.bbands(data['Close'])
print(bands)
a=mpf.make_addplot(bands['BBL_5_2.0'],color='blue')
b=mpf.make_addplot(bands['BBM_5_2.0'],color='red')
c=mpf.make_addplot(bands['BBU_5_2.0'],color='green')


#atr
atr=ta.atr(data['High'],data['Low'],data['Close'])
print(atr)
d=mpf.make_addplot(atr,color='black',panel=1)
mpf.plot(data,addplot=[a,b,c,d],type='candle',style='yahoo')

