

import yfinance as yf
import pandas_ta as ta
from backtesting import Strategy,Backtest
from backtesting.lib import resample_apply
import time

# def get_sma(closing_price,period):
#     sma=ta.sma(closing_price,period)
#     return sma

# def get_bollinger_band(closing_price, period):
#     bb=ta.bbands(closing_price, period)
#     return bb[f'BBL_{period}_2.0'],bb[f'BBU_{period}_2.0']

def get_supertrend(closing_price, high, low, period):
    st=ta.supertrend(closing_price, high, low, period)
    # print(st)
    return st[f'SUPERTd_{period}_3.0']

def get_supertrend2(closing_price, high, low, period):
    st=ta.supertrend(closing_price, high, low, period)
    # print(st)
    return st[f'SUPERT_{period}_3.0']
class SupertrendStrategy(Strategy):
    n1 = 50
    gran = '10min'

    def init(self):
        self.super = resample_apply(self.gran, get_supertrend, self.data.Close, self.data.High, self.data.Low, self.n1)
        self.super2 = resample_apply(self.gran, get_supertrend2, self.data.Close, self.data.High, self.data.Low, self.n1)

    def next(self):
        # Buy condition
        if self.super[-1] > self.super[-2]:
            if self.position.is_short:
                self.position.close()
            self.buy()
        
        # Sell condition
        if self.super[-1] < self.super[-2]:
            if self.position.is_long:
                self.position.close()
            self.sell()

# ticker='RELIANCE.NS'
# data=yf.download(ticker,period='10d',interval='5m')
# print(data)

import pandas as pd
data=pd.read_csv('/Users/algotrading2024/batch 28/eth_5m.csv')

data.rename(columns={'close':'Close','high':'High','low':'Low','open':'Open','timestamp':'Date'},inplace=True)
data['Date']=pd.to_datetime(data['Date'])
data.drop(columns=['symbol','trade_count','vwap'],inplace=True)
data.set_index('Date',inplace=True)
print(data)
#feed only 10_000 rows
data=data.iloc[:10000]


# print(get_bollinger_band(data['Close'],20))

print(get_supertrend(data['Close'], data['High'], data['Low'], 10))

bt=Backtest(data,SupertrendStrategy,cash=50000)
output=bt.run()
print(output)
# bt.plot()



def custom_optimization(stats):
    return stats['Win Rate [%]'] * stats['Return [%]']



l1=['10min','15min','30min','60min','120min']
stats=bt.optimize(gran=l1,maximize='Return [%]')
print(stats)
print('GOOG',stats['_strategy'])
# bt.plot()