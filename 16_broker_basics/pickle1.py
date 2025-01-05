import pickle
import datetime as dt
import pandas as pd

strategy_name='temple'

def store(data):
    pickle.dump(data,open(f'{strategy_name}-{dt.date.today()}.pickle','wb'))

def load():
    return pickle.load(open(f'{strategy_name}-{dt.date.today()}.pickle', 'rb'))



d=pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')[2]
# print(d)

store(d)
data=load()
print(data)