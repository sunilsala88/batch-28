#yfinanca
import yfinance as yf
data=yf.download('RELIANCE.NS',period='5d',interval='1m')
print(data)

#alpaca

from credentials import api_key,secret_key
from alpaca.data.historical.stock import StockHistoricalDataClient

# setup stock historical data client
stock_historical_data_client = StockHistoricalDataClient(api_key, secret_key)

from datetime import datetime,timedelta
from zoneinfo import ZoneInfo
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

from alpaca.data.historical.crypto import CryptoHistoricalDataClient
# setup crypto historical data client
crypto_historical_data_client = CryptoHistoricalDataClient()

from alpaca.data.requests import CryptoBarsRequest
# get historical bars by symbol
# ref. https://docs.alpaca.markets/reference/cryptobars-1
symbol = "ETH/USD"
now = datetime.now(ZoneInfo("America/New_York"))
s=datetime(2023,1,1,0,0,0,tzinfo=ZoneInfo("America/New_York"))
e=datetime(2023,12,1,0,0,0,tzinfo=ZoneInfo("America/New_York"))
req = CryptoBarsRequest(
    symbol_or_symbols = [symbol],
    timeframe=TimeFrame(amount = 5, unit = TimeFrameUnit.Minute), # specify timeframe
    start = s,                          # specify start datetime, default=the beginning of the current day.
    end_date=e,                                        # specify end datetime, default=now
    # limit = 2,                                               # specify limit
)
history_df2=crypto_historical_data_client.get_crypto_bars(req).df
history_df2

history_df2.reset_index().drop('symbol',axis=1).set_index('timestamp')
history_df2.to_csv('eth_5m.csv')
print(history_df2)