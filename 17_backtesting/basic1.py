#environment
#3.12.2
#pip install backtesting
#numpy pip install numpy==1.26.4
#bokeh pip install bokeh==2.4.3
#No module named 'pkg_resources' pip install setuptools
#yfinance pip install yfinance==0.2.37

from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG


class SmaCross(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()


bt = Backtest(GOOG, SmaCross,
              cash=10000, commission=.002,
              exclusive_orders=True)

output = bt.run()
bt.plot()
print(output)
print(output['_trades'].to_csv('trades.csv'))