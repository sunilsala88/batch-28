from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG


class SmaCrossWithTrailingStop(Strategy):
    n1 = 10
    n2 = 20
    trailing_stop_pct = 0.1  # 5% trailing stop loss

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2) :
            if self.position.is_short:
                self.position.close()
            self.buy()
        elif crossover(self.sma2, self.sma1):
            if self.position.is_long:
                self.position.close()
            self.sell()

        # Update trailing stop loss for any open positions
        # for trade in self.trades:
        #     if trade.is_long:
        #         trade.sl = max(trade.sl or 0, self.data.Close[-1] * (1 - self.trailing_stop_pct))

        #     elif trade.is_short:
        #         trade.sl = min(trade.sl or float('inf'), self.data.Close[-1] * (1 + self.trailing_stop_pct))

bt = Backtest(GOOG, SmaCrossWithTrailingStop,
              cash=10000, commission=.002,
              exclusive_orders=True)

output = bt.run()
print(output)
bt.plot()
