from alpaca.data.live.crypto import CryptoDataStream
from credentials import api_key,secret_key
import certifi
import os

import pendulum as dt
time_zone="UTC"
print(dt.now(time_zone))
#for windows ssl error
os.environ['SSL_CERT_FILE'] = certifi.where()
crypto_data_stream_client=CryptoDataStream(api_key,secret_key)
async def crypto_data_stream_handler(data):
    print(data)
    print(dt.now(time_zone))

symbol=['BTC/USD','ETH/USD']
# crypto_data_stream_client.subscribe_trades(crypto_data_stream_handler, *symbol)

crypto_data_stream_client.subscribe_quotes(crypto_data_stream_handler, *symbol)
crypto_data_stream_client.run()