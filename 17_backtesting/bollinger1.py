

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

class bollinger_strategy(Strategy):
    n1=20


    def init(self):
        print('this is data inside init')
        closing_price=self.data.df['Close']
        self.lower,self.upper=self.I(get_bollinger_band,closing_price,self.n1)


    def next(self):
        pass
        # print(self.data.df)
        # time.sleep(1)        
        #buy condition
        if self.lower[-1] > self.data.Close[-1] :
            print('buy')
            if self.position.is_short:
                self.position.close()
            self.buy()
        
        #sell condition
        if self.upper[-1] < self.data.Close[-1] :
            print('sell')
            if self.position.is_long:
                self.position.close()
            self.sell()


data=yf.download('RELIANCE.NS',period='10y')
print(data)
print(get_sma(data['Close'], 20))

print(get_bollinger_band(data['Close'],20))

bt=Backtest(data,bollinger_strategy,cash=5000)
output=bt.run()
print(output)
bt.plot()
