from backtesting import Backtest, Strategy


import pandas as pd
# from ta.utils import dropna
# from ta.volatility import BollingerBands
# from ta.trend import sma_indicator,ema_indicator
import pandas_ta as ta
from backtesting.lib import resample_apply
def EMA1(closing_data,l1):
    return ta.ema(closing_data,l1)



def SMA1(closing_data,l):
    sma2 = ta.sma(closing_data,l)
    return sma2

def SMA2(closing_data,l):
    sma2 = ta.sma(closing_data,l)
    return sma2


class Sma_Strategy(Strategy):
    gran='5min'
    n1=30
    n2=100
    def init(self):
        # closing_price=self.data.Close.s
        # self.sma1=self.I(SMA1,closing_price,self.n1)
        # self.sma2=self.I(SMA2,closing_price,self.n2)

        self.sma1 = resample_apply(self.gran, SMA1,self.data.Close.s,self.n1)
        self.sma2 = resample_apply(self.gran, SMA2,self.data.Close.s,self.n2)



    def next(self):
        if self.sma1[-1]<self.sma2[-1] and self.sma1[-2]>self.sma2[-2]:
            self.buy()
        if self.sma1[-1]>self.sma2[-1] and self.sma1[-2]<self.sma2[-2]:
            self.position.close()
        


# import yfinance as yf
# data=yf.download('GOOG',start='2020-06-24',end='2024-06-29',interval='1d')
# print(data)


# from ib_insync import *
# # util.startLoop()  # uncomment this line when in a notebook
# import datetime as dt
# import pandas as pd
# ib = IB()
# ib.connect('127.0.0.1', 7497, clientId=66)

# def last_day_of_month(year, month):
#     next_month = month % 12 + 1
#     next_year = year + month // 12
#     last_day = dt.date(next_year, next_month, 1) - dt.timedelta(days=1)
#     return last_day

# name='GOOG'
# contract2=Stock(name,'SMART','USD')
# contract2=ib.qualifyContracts(contract2)[0]
# # year=5
# print(contract2)

# final_data=pd.DataFrame()


# for month in range(1,13):

#     end_time=last_day_of_month(2023, month)
#     print(end_time)
#     bars = ib.reqHistoricalData(
#         contract2, endDateTime=end_time, durationStr='1 M',
#         barSizeSetting='1 min', whatToShow='TRADES', useRTH=True,formatDate=1)
#     df1 = util.df(bars)
#     print(df1)
#     final_data=pd.concat([final_data,df1],axis=0).drop_duplicates()
    
# print(final_data)

# d1={'date':'Date','open':'Open','high':'High','low':'Low','close':'Close','volume':'Volume'}
# final_data.rename(columns =d1, inplace = True) 
# final_data.set_index('Date',inplace=True)
# final_data.to_csv(f'{name}_1min.csv')

# Read CSV from GitHub link
url = 'https://raw.githubusercontent.com/sunilsala88/backtesting-july-2024/main/GOOG_1min.csv'
data = pd.read_csv(url)
data=data.iloc[0:30000]
data['Date']=data['Date'].str[:-6]
print(data)
data['Date']=pd.to_datetime(data['Date'])
data['Date']=data['Date'].dt.tz_localize(None)
data.set_index('Date',inplace=True)
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)
# data.drop
print(data)

# data=data['2023-01-03 14:30:00':'2023-06-03 14:30:00']
# print(data)
bt = Backtest(data, Sma_Strategy,
              cash=10000, commission=.002,
              exclusive_orders=True)

output = bt.run()
print(output)
# print(output['_trades'])
# bt.plot()

# stats=bt.optimize(n1=range(5,100,5),n2=range(100,200,5),maximize='Return [%]')
# print(stats)
# print('GOOG',stats['_strategy'])
# bt.plot()



l1=['5min','15min','30min','60min','120min','240min']
stats=bt.optimize(gran=l1,maximize='Return [%]')
print(stats)
print('GOOG',stats['_strategy'])
# bt.plot()