import yfinance as yf
import pandas as pd
instrument=yf.Ticker(ticker='TSLA')
#info
print(instrument.info.get('marketCap'))


data=pd.read_html('https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average')

# print(data)
df2=data[2]
df2=df2[['Company','Symbol','Date added']]
print(df2)
beta=[]
for name in df2['Symbol']:
    try:
        instrument=yf.Ticker(ticker=name)
        b=instrument.info.get('beta')
        if b:
            beta.append(b)

    except:
        print(name)


print(beta.sort())
print(beta[:5])


