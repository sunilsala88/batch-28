

import yfinance as yf
import pandas_ta as ta
from backtesting import Strategy,Backtest
import time

def get_sma(closing_price,period):
    sma=ta.sma(closing_price,period)
    return sma

class sma_strategy(Strategy):
    n1=50
    n2=30
    sl1=0.1

    def init(self):
        # print('this is data inside init')
        closing_price=self.data.df['Close']
        self.sma1=self.I(get_sma,closing_price,self.n1)
        self.sam2=self.I(get_sma, closing_price, self.n2)

    def next(self):
    
        # print(self.data.df)
        # time.sleep(1)        
        #buy condition
        if self.sma1[-1]>self.sam2[-1] and self.sma1[-2]<self.sam2[-2]:
            if self.position.is_short:
                self.position.close()
            self.buy(sl=self.data.Close[-1]*(1-self.sl1))

        #sell conditon
        elif self.sma1[-1]<self.sam2[-1] and self.sma1[-2]>self.sam2[-2]:
            if self.position.is_long:
                self.position.close()
            self.sell(sl=self.data.Close[-1]*(1+self.sl1))

ticker='HDFCBANK.NS'
data=yf.download(ticker,period='5y')
print(data)
print(get_sma(data['Close'], 20))

bt=Backtest(data,sma_strategy,cash=50000)
output=bt.run()
print(output)
bt.plot()

#overfitting



