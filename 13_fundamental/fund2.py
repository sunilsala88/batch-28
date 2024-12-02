# import yfinance as yf
# import pandas as pd
# instrument=yf.Ticker(ticker='BPCL.NS')

# print(instrument.cash_flow)
# print(instrument.get_earnings_dates())



from finvizfinance.quote import finvizfinance

stock = finvizfinance('NVDA')

stock_fundament = stock.ticker_fundament()

print(stock_fundament)