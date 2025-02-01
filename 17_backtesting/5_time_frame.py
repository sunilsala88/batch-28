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
        




# Read CSV from GitHub link
url = 'https://raw.githubusercontent.com/sunilsala88/backtesting-july-2024/main/GOOG_1min.csv'
data = pd.read_csv(url)
data=data.iloc[0:20000]
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
bt.plot()

# stats=bt.optimize(n1=range(5,100,5),n2=range(100,200,5),maximize='Return [%]')
# print(stats)
# print('GOOG',stats['_strategy'])
# bt.plot()



l1=['5min','15min','30min','60min','120min','240min']
stats=bt.optimize(gran=l1,maximize='Return [%]')
print(stats)
print('GOOG',stats['_strategy'])
# bt.plot()