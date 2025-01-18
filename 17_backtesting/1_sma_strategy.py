

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
            self.buy()

        #sell conditon
        elif self.sma1[-1]<self.sam2[-1] and self.sma1[-2]>self.sam2[-2]:
            if self.position.is_long:
                self.position.close()
            self.sell()

ticker='HDFCBANK.NS'
data=yf.download(ticker,period='5y')
print(data)
print(get_sma(data['Close'], 20))

bt=Backtest(data,sma_strategy,cash=50000)
output=bt.run()
print(output)
# bt.plot()

#overfitting


#indicator optimization
l1=range(50,100,3)
l2=range(10,40,3)
stats=bt.optimize(n1=l1,n2=l2,maximize='Return [%]')
print(stats)
print(ticker,stats['_strategy'])
# bt.plot()


def custom_optimization(stats):
    return stats['Win Rate [%]'] * stats['Return [%]']


#optimize multiple parameters at once
# l1=range(50,100,3)
# l2=range(10,40,3)
stats=bt.optimize(n1=l1,n2=l2,maximize=custom_optimization)
print(stats)
print(ticker,stats['_strategy'])
bt.plot()
