# import yfinance as yf
# import pandas as pd
# instrument=yf.Ticker(ticker='BPCL.NS')

# print(instrument.cash_flow)
# print(instrument.get_earnings_dates())



# from finvizfinance.quote import finvizfinance

# stock = finvizfinance('TSLA')

# stock_fundament = stock.ticker_fundament()

# print(stock_fundament)

# print(stock.ticker_news())

# inside_trader_df = stock.ticker_inside_trader()
# print(inside_trader_df)


from finvizfinance.screener.overview import Overview

foverview = Overview()
filters_dict = {'Index':'S&P 500'}
foverview.set_filter(filters_dict=filters_dict)
df = foverview.screener_view()
print(df)
