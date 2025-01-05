


import logging
import datetime as dt
import time
import pandas as pd
strategy_name='temple'
logging.basicConfig(level=logging.INFO, filename=f'{strategy_name}_{dt.date.today()}.log',filemode='a',format="%(asctime)s - %(message)s")

print('hello')
logging.info('hello')

def strategy():
    print('checking logic now')
    logging.info('checking logic now ')
    d=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')[2]
    logging.info(d)


while True:
    ct=dt.datetime.now()
    print(ct)
    if ct.second==1:
        strategy()
    time.sleep(1)
    