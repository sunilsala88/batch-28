import yfinance as yf
import datetime as dt
end=dt.datetime.now().date()
start=(dt.datetime.now()-dt.timedelta(days=600)).date()

# data=yf.download(tickers='TSLA',interval='1m',start='2024-11-25',end='2024-12-30')
data=yf.download(tickers='ETH-USD',interval='1h',start=start,end=end)
print(data)


#bitcoin
#ethusd

#time zone
# import pytz
# print(pytz.all_timezones)
# data.reset_index(inplace=True)
# print(data)
# data['Datetime']=data['Datetime'].dt.tz_convert('Asia/Kolkata')
# print(data)
# data['Datetime']=data['Datetime'].dt.tz_convert('UTC')
# print(data)
# data['Datetime']=data['Datetime'].dt.tz_convert(None)
# data['Datetime']=data['Datetime'].dt.tz_localize(None)
# print(data)
# # UTC-0000

# d={'Open':'first','High':'max','Low':'min','Close':'last','Volume':'sum'}
# new_data=data.resample('60min').agg(d)
# new_data.dropna(inplace=True)
# print(new_data.head(20))

#plot
#matplotlib

import mplfinance as mpf

mpf.plot(data=data,type='candle',style='yahoo')