from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

# no keys required for crypto data
client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD", "ETH/USD"],
                        timeframe=TimeFrame.Day,
                        start=datetime(2022, 7, 1),
                        end=datetime(2022, 9, 1)
                 )

bars = client.get_crypto_bars(request_params)

# convert to dataframe
print(bars.df)


from credentials import api_key,secret_key
from alpaca.data.historical import StockHistoricalDataClient
from datetime import datetime,timedelta
from zoneinfo import ZoneInfo
from alpaca.data.requests import StockBarsRequest ,StockTradesRequest,StockQuotesRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

# setup stock historical data client
stock_historical_data_client = StockHistoricalDataClient(api_key, secret_key)

symbol='GOOG'


now = datetime.now(ZoneInfo("America/New_York"))


req = StockBarsRequest(
    symbol_or_symbols = symbol,
    timeframe=TimeFrame(amount = 5, unit = TimeFrameUnit.Minute), # specify timeframe
    start = now - timedelta(days = 100),                          # specify start datetime, default=the beginning of the current day.
    # end_date=None,                                        # specify end datetime, default=now
    # limit = 2,                                               # specify limit
)
data=stock_historical_data_client.get_stock_bars(req).df
print(data)
