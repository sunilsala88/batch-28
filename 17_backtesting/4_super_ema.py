





import pandas_ta as ta
import pandas as pd
from backtesting import Strategy, Backtest
import yfinance as yf
import pandas_ta as ta
from backtesting.lib import resample_apply
import time
def supertrend1(high_data,low_data,close_data):
    o=ta.supertrend(high_data,low_data,close_data,length=10)
    print(o)
    return o['SUPERTd_10_3.0']
def supertrend2(high_data,low_data,close_data):
    o=ta.supertrend(high_data,low_data,close_data,length=10)
    return o['SUPERT_10_3.0']
def ema(close_data,period=9):
    return ta.ema(close_data,length=period)


class supertrend(Strategy):
    
    n1=9

    def init(self):
        self.super1=self.I(supertrend1,self.data.High.s,self.data.Low.s,self.data.Close.s)
        # self.super2=self.I(supertrend2,self.data.High.s,self.data.Low.s,self.data.Close.s)
        
        # self.ema_hour=self.I(ema,self.data.Close.s,self.n1)

        self.daily_ema = resample_apply('D', ema,self.data.Close.s,self.n1)

    def next(self):
      
        if self.super1[-1]>0 and self.data.Close[-1]> self.daily_ema[-1]:


            if self.position.is_short:
                self.position.close()
                self.buy()



            elif not self.position:  
                self.buy()


        elif self.super1[-1]<0 and self.data.Close[-1]<self.daily_ema[-1]:
            if self.position.is_long:
                self.position.close()
            self.sell()


# data=pd.read_csv('/Users/algotrading2024/batch 27/backtesting/SPY.csv')
# print(data)
# data.drop(['symbol','trade_count','vwap','volume'],axis=1,inplace=True)
# data.rename(columns={'timestamp':'Date','open':'Open','high':'High','low':'Low','close':'Close'},inplace=True)
# data['Date']=pd.to_datetime(data['Date'])
# data.set_index('Date',inplace=True)
# print(data)
# data=data.iloc[:10000,]

import yfinance as yf
data=yf.download('^NSEI',period='700d',interval='1h')
print(data)

s1=supertrend1(data.High,data.Low,data.Close)
s2=supertrend2(data.High,data.Low,data.Close)
e1=ema(data.Close,10)
print(s1)
print(s2)
print(e1)

bt=Backtest(data,supertrend,cash=25000)
output=bt.run()
print(output)
# print(output['_trades'].to_csv('trades.csv'))
bt.plot()