

import yfinance as yf
import pandas_ta as ta
from backtesting import Strategy,Backtest
import time

def get_sma(closing_price,period):
    sma=ta.sma(closing_price,period)
    return sma

def get_bollinger_band(closing_price, period):
    bb=ta.bbands(closing_price, period)
    return bb[f'BBL_{period}_2.0'],bb[f'BBU_{period}_2.0']

def get_supertrend(closing_price, high, low, period):
    st=ta.supertrend(closing_price, high, low, period)
    print(st)
    return st[f'SUPERTd_{period}_3.0']

def get_supertrend2(closing_price, high, low, period):
    st=ta.supertrend(closing_price, high, low, period)
    print(st)
    return st[f'SUPERT_{period}_3.0']
class supertrend_strategy(Strategy):
    n1=20


    def init(self):
        print('this is data inside init')
        closing_price=self.data.df['Close']
        self.super=self.I(get_supertrend,self.data.df['Close'],self.data.df['High'],self.data.df['Low'],self.n1)
        self.super2=self.I(get_supertrend2,self.data.df['Close'],self.data.df['High'],self.data.df['Low'],self.n1)
        

    def next(self):
        pass
        # # print(self.data.df)
        # # time.sleep(1)        
        #buy condition
        if self.super[-1] > self.super[-2] :
            print('buy')
            if self.position.is_short:
                self.position.close()
            self.buy()
        
        #sell condition
        if self.super[-1] < self.super[-2]  :
            print('sell')
            if self.position.is_long:
                self.position.close()
            self.sell()


data=yf.download('RELIANCE.NS',period='10y')
print(data)
# print(get_sma(data['Close'], 20))

# print(get_bollinger_band(data['Close'],20))

print(get_supertrend(data['Close'], data['High'], data['Low'], 10))

bt=Backtest(data,supertrend_strategy,cash=5000)
output=bt.run()
print(output)
bt.plot()
