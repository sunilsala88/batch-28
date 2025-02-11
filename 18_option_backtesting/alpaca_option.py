
import datetime as dt

api_key='PKCGQ99MC5FQA1P8ZSRE'
secret_key="rkWLI1F2poiTbuERdzozfOLgVV6mrFKTH27Ugvb1"

import json
import pickle
import sys
from zoneinfo import ZoneInfo
from alpaca.data.live.option import *
from alpaca.data.live.stock import *
from alpaca.data.historical.option import *
from alpaca.data.historical.stock import *
from alpaca.data.requests import *
from alpaca.data.timeframe import *
from alpaca.trading.client import *
from alpaca.trading.stream import *
from alpaca.trading.requests import *
from alpaca.trading.enums import *
from alpaca.common.exceptions import APIError

from alpaca.data.models import OptionsSnapshot
paper = True # Please do not modify this. This example is for paper trading only.
trade_api_url = None
trade_api_wss = None
data_api_url = None
option_stream_data_wss = None

import logging
logging.basicConfig(level=logging.INFO, filename=f'option_strategy_{dt.date.today()}',filemode='a',format="%(asctime)s - %(message)s")

try:
    order_filled_dataframe=pd.read_csv('order_filled_list.csv')
    order_filled_dataframe.set_index('time',inplace=True)

except:
    column_names = ['time','ticker','price','action','type1','stop_price']
    order_filled_dataframe = pd.DataFrame(columns=column_names)
    order_filled_dataframe.set_index('time',inplace=True)




# setup clients
trade_client = TradingClient(api_key=api_key, secret_key=secret_key, paper=paper, url_override=trade_api_url)
acct = trade_client.get_account()


ticker='SPY'
quantity=1
currency='USD'
strike_limit=6


current_time=dt.datetime.now()
first_trade_flag=0
short_price=3
long_price=0.5
start_hour,start_min=20,6
end_hour,end_min=20,11
all_option_contract={}
shortlist_option={}

# setup clients
stock_historical_data_client = StockHistoricalDataClient(api_key, secret_key, url_override = data_api_url)
StockLatestTradeRequest = StockLatestTradeRequest(symbol_or_symbols=[ticker])
d=stock_historical_data_client.get_stock_latest_trade(StockLatestTradeRequest)
print(d)


current_price=round(d[ticker].price)
print(current_price)

expiry=(dt.datetime.now()+dt.timedelta(days=1)).date()
print(expiry)
# expiry=(dt.datetime.now()).date()

# Check if the file exists


def store(data):
    pickle.dump(data,open(f'data{dt.date.today()}.pickle','wb'))

def load():
    return pickle.load(open(f'data{dt.date.today()}.pickle', 'rb'))

def updat_order_csv(name,price,action,type1,stop_price):
    global order_filled_dataframe
    a=[name,price,action,type1,stop_price]
    order_filled_dataframe.loc[dt.datetime.now()] = a
    order_filled_dataframe.to_csv('order_filled_list.csv')


try:
    data=load()
    print(data)
    print('data loaded from pickle file')
    shortlist_option=data
    first_trade_flag=shortlist_option['first_trade_flag']
except:
    print('no data to read')


def get_option_data():

    # setup option historical data client
    option_historical_data_client = OptionHistoricalDataClient(api_key, secret_key, url_override = data_api_url)

    # get option chain by underlying_symbol
    req = OptionChainRequest(underlying_symbol = ticker,
                            expiration_date=expiry,
                            strike_price_gte=current_price-strike_limit,
                            strike_price_lte=current_price+strike_limit
                            )
    response=option_historical_data_client.get_option_chain(req)
    # print(response)
    data = []
    for symbol, details in response.items():
        
        details=dict(details)
        # print(symbol)
        # print(details['greeks'])
        if not details['greeks']: continue
        row = {
            'symbol': symbol,
            'delta': dict(details['greeks'])['delta'],
            'gamma': dict(details['greeks'])['gamma'],
            'rho': dict(details['greeks'])['rho'],
            'theta': dict(details['greeks'])['theta'],
            'vega': dict(details['greeks'])['vega'],
            'implied_volatility': float(details['implied_volatility']),
            'ask_exchange': dict(details['latest_quote'])['ask_exchange'],
            'ask_price': dict(details['latest_quote'])['ask_price'],
            'ask_size': dict(details['latest_quote'])['ask_size'],
            'bid_exchange': dict(details['latest_quote'])['bid_exchange'],
            'bid_price': dict(details['latest_quote'])['bid_price'],
            'bid_size': dict(details['latest_quote'])['bid_size'],
            'quote_conditions': dict(details['latest_quote'])['conditions'],
            'quote_timestamp': dict(details['latest_quote'])['timestamp'],
            'trade_conditions': dict(details['latest_trade'])['conditions'],
            'trade_exchange': dict(details['latest_trade'])['exchange'],
            'trade_price': dict(details['latest_trade'])['price'],
            'trade_size': dict(details['latest_trade'])['size'],
            'trade_timestamp': dict(details['latest_trade'])['timestamp']
        }
        data.append(row)


    df = pd.DataFrame(data)
    df['strike']=df['symbol'].str[-6:-3]


    df['strike']=df['strike'].astype(int)

    df['right']=df['symbol'].str[-9]
    df.sort_values(by=['strike', 'right'], inplace=True)
    df.set_index('symbol', inplace=True)
    print(df)
    df.to_csv('live_option_data.csv')
    return df

get_option_data()

def get_nearest_cent_option(df,cent,right):
    df1=df[df['right']==right]
    option_name=(df1['trade_price'] - cent).abs().idxmin()
    return option_name

def buy_condor(shortlist_option):
    for name,data in shortlist_option.items() :   
        if name.startswith("short"):
            direction=OrderSide.SELL
        else:
            direction=OrderSide.BUY
        
        n_name=shortlist_option[name]['name']
        # place market order
        req = MarketOrderRequest(
            symbol = n_name,
            qty = 1,
            side = direction,
            type = OrderType.MARKET,
            time_in_force = TimeInForce.DAY
        )
        res = trade_client.submit_order(req)
        print(res)



        shortlist_option[name]['order_placed']=True   
        updat_order_csv(n_name,df.loc[n_name,'trade_price'],direction,'MKT',0) 
        time.sleep(3)
    return shortlist_option


def manage_iron_condor(shortlist_option,option_leg,new_price):

    positions = trade_client.get_all_positions()
    pos_df=pd.DataFrame([dict(position) for position in positions])


    pos_df['name']=[cont for cont in pos_df['symbol']]
    pos_df=pos_df[pos_df['qty']!=0]
    print(pos_df)
    #close option leg
    leg_name=shortlist_option[option_leg].get('name')
    print(leg_name)
    if leg_name in pos_df['name'].to_list():
        print('inside')
        leg_name1=shortlist_option[option_leg].get('name')
        req = MarketOrderRequest(
            symbol = leg_name1,
            qty = 1,
            side = OrderSide.BUY,
            type = OrderType.MARKET,
            time_in_force = TimeInForce.DAY
        )
        res = trade_client.submit_order(req)
        print(res)
        updat_order_csv(leg_name1,df.loc[leg_name1,'trade_price'],'BUY','MKT',0)

        #update option leg
        new_option=get_nearest_cent_option(df,new_price,leg_name1[9])
        shortlist_option[option_leg]={'name':new_option,'buy_price':df.loc[new_option,'trade_price']}

        
        req = MarketOrderRequest(
            symbol = new_option,
            qty = 1,
            side = OrderSide.SELL,
            type = OrderType.MARKET,
            time_in_force = TimeInForce.DAY
        )
        res = trade_client.submit_order(req)
        print(res)


        updat_order_csv(new_option,df.loc[new_option,'trade_price'],'SELL','MKT',0)

    return shortlist_option





def stop_order_on_leg(shortlist_option,df):
    #place for call option
    print('inside stop order leg')
    cont_name=shortlist_option['short_call_option'].get('name')


    p=df.loc[cont_name,'trade_price']
    print(p)

    # ord1=StopOrder('BUY',quantity,p*2)
    # p1=ib.placeOrder(cont,ord1)

    # stop order
    # req = StopOrderRequest(
    #                     symbol = cont_name,
    #                     qty = 1,
    #                     side = OrderSide.BUY,
    #                     time_in_force = TimeInForce.DAY,
    #                     stop_price = p*2
    #                     )

    # res = trade_client.submit_order(req)
    # res


    updat_order_csv(cont_name,df.loc[cont_name,'trade_price'],'BUY','STP',p*2)
    # print(p1)
    shortlist_option['short_call_option']['stop_price']=p*2
    # shortlist_option['short_call_option']['stop_order_object']=ord1

    #place for put option

    cont_name2=shortlist_option['short_put_option'].get('name')
    p=df.loc[cont_name2,'trade_price']

    # req = StopOrderRequest(
    #                     symbol = cont_name2,
    #                     qty = 1,
    #                     side = OrderSide.BUY,
    #                     time_in_force = TimeInForce.DAY,
    #                     stop_price = p*2
    #                     )

    # res = trade_client.submit_order(req)
    # res

    # ord1=StopOrder('BUY',quantity,p*2)
    # p1=ib.placeOrder(cont,ord1)
    
    updat_order_csv(cont_name2,df.loc[cont_name2,'trade_price'],'BUY','STP',p*2)
    # print(p1)
    shortlist_option['short_put_option']['stop_price']=p*2
    # shortlist_option['short_put_option']['stop_order_object']=ord1
    
    return shortlist_option


def close_position(shortlist_option,op_name):

    cont_name=shortlist_option[op_name].get('name')
    print(cont_name)
    #closing option position


    trade_client.close_position(symbol_or_asset_id = cont_name,
    close_options = ClosePositionRequest(qty = "1"))

    


def change_stop_order_price(shortlist_option,option_type):

    #cancel stop order
    #place new stop order half the price
    cont_name2=shortlist_option[option_type].get('name')
   
    p=df.loc[cont_name2,'trade_price']
    print(p)
    sp=shortlist_option[option_type]['stop_price']

    shortlist_option[option_type]['stop_price']=sp-sp*0.05


    updat_order_csv(cont_name2,df.loc[cont_name2,'trade_price'],'BUY','UPDATE',sp-sp*0.05)
 
    return shortlist_option



def close_all_position():

    if shortlist_option['short_call_option'].get('close_flag'):
        op_name='short_put_option'
    else:
         op_name='short_call_option'
    cont_name=shortlist_option[op_name].get('name')
    print(cont_name)

    trade_client.close_position(
    symbol_or_asset_id = cont_name,
    close_options = ClosePositionRequest(qty = "1"))



# import xlwings as xw
# wb = xw.Book('Data2.xlsx')
# sheet = wb.sheets['Sheet1']

import time
while True:
    time.sleep(1)
    df=get_option_data()
    # print(df)
    # sheet['A2'].value = df

    if first_trade_flag==0: #and dt.datetime.now()>dt.datetime(current_time.year,current_time.month,current_time.day,start_hour,start_min):
        print('taking trade')


        short_call_option=get_nearest_cent_option(df,short_price,'C')
        shortlist_option['short_call_option']={'name':short_call_option,'buy_price':df.loc[short_call_option,'trade_price']}

        short_put_option=get_nearest_cent_option(df,short_price,'P')
        shortlist_option['short_put_option']={'name':short_put_option,'buy_price':df.loc[short_put_option,'trade_price']}

        long_call_option=get_nearest_cent_option(df,long_price,'C')
        shortlist_option['long_call_option']={'name':long_call_option,'buy_price':df.loc[long_call_option,'trade_price']}

        long_put_option=get_nearest_cent_option(df,long_price,'P')
        shortlist_option['long_put_option']={'name':long_put_option,'buy_price':df.loc[long_put_option,'trade_price']}

        print(short_call_option,short_put_option,long_call_option,long_put_option)

        print('short_call_option',short_call_option,df.loc[short_call_option,'trade_price'])
        print('short_put_option',short_put_option,df.loc[short_put_option,'trade_price'])
        print("long_call_option",long_call_option,df.loc[long_call_option,'trade_price'])
        print("long_put_option",long_put_option,df.loc[long_put_option,'trade_price'])

        first_trade_flag=1

        shortlist_option=buy_condor(shortlist_option)
        shortlist_option['first_trade_flag']=1
        store(shortlist_option)
        print(shortlist_option)
        print('seeping for few seconds')
        # break
        # # time.sleep(10)

        
        
    elif first_trade_flag==1:
            # check if placed order price doubled
            print('order placed 1')
            print(shortlist_option) 
            print(df.loc[shortlist_option['short_call_option'].get('name'),'trade_price'],df.loc[shortlist_option['short_put_option'].get('name'),'trade_price'])
            if shortlist_option['short_call_option'].get('buy_price')*2<df.loc[shortlist_option['short_call_option'].get('name'),'trade_price']:
                shortlist_option=manage_iron_condor(shortlist_option,'short_put_option',shortlist_option['short_call_option'].get('buy_price')*2)
                first_trade_flag=2
                shortlist_option['first_trade_flag']=2
                store(shortlist_option)
            if shortlist_option['short_put_option'].get('buy_price')*2<df.loc[shortlist_option['short_put_option'].get('name'),'trade_price']:
                shortlist_option=manage_iron_condor(shortlist_option,'short_call_option',shortlist_option['short_put_option'].get('buy_price')*2)
                first_trade_flag=2
                shortlist_option['first_trade_flag']=2
                store(shortlist_option)
                

    elif first_trade_flag==2:
            #place stop order on both legs
            print('first trade 2')
            print('will be placing stop order')
            # time.sleep(10)
            shortlist_option=stop_order_on_leg(shortlist_option,df)
            first_trade_flag=3 
            shortlist_option['first_trade_flag']=3
            store(shortlist_option)
 


    elif first_trade_flag==3:
            print('first trade 3')
            print(shortlist_option)
            #if call sell price 
       
            if df.loc[shortlist_option['short_call_option'].get('name'),'trade_price']>shortlist_option['short_call_option']['stop_price']:
                updat_order_csv(shortlist_option['short_call_option'].get('name'),df.loc[shortlist_option['short_call_option'].get('name'),'trade_price'],'BUY','STPFill',0)
                print('stop loss of short call option is executing')
                #closing a position
                close_position(shortlist_option,'short_call_option')
                shortlist_option['short_call_option']['close_flag']=True
                shortlist_option['short_put_option']['close_flag']=False
    


                shortlist_option=change_stop_order_price(shortlist_option,'short_put_option')
                first_trade_flag=4
                shortlist_option['first_trade_flag']=4
                store(shortlist_option)

            elif df.loc[shortlist_option['short_put_option'].get('name'),'trade_price']>shortlist_option['short_put_option']['stop_price']:
                updat_order_csv(shortlist_option['short_put_option'].get('name'),df.loc[shortlist_option['short_put_option'].get('name'),'trade_price'],'BUY','STPFill',0)
                print('stop loss of short put option is executing')
                #closing a position
                close_position(shortlist_option,'short_put_option')


                shortlist_option['short_call_option']['close_flag']=False
                shortlist_option['short_put_option']['close_flag']=True
  
                shortlist_option=change_stop_order_price(shortlist_option,'short_call_option')
                first_trade_flag=4
                shortlist_option['first_trade_flag']=4
                store(shortlist_option)
   
                


    elif first_trade_flag==4:
            print('first flag is 4')
            print(shortlist_option)
            #check if current stop price has breached

            if df.loc[shortlist_option['short_call_option'].get('name'),'trade_price']>shortlist_option['short_call_option']['stop_price'] and shortlist_option['short_call_option'].get('close_flag')==False:

                updat_order_csv(shortlist_option['short_call_option'].get('name'),df.loc[shortlist_option['short_call_option'].get('name'),'trade_price'],'BUY','STPFill',0)
                print('stop loss of short call option is executing')
                #closing a position
                close_position(shortlist_option,'short_call_option')

                first_trade_flag=5
                shortlist_option['first_trade_flag']=5
                store(shortlist_option)

            elif df.loc[shortlist_option['short_put_option'].get('name'),'trade_price']>shortlist_option['short_put_option']['stop_price'] and shortlist_option['short_put_option'].get('close_flag')==False :
                updat_order_csv(shortlist_option['short_put_option'].get('name'),df.loc[shortlist_option['short_put_option'].get('name'),'trade_price'],'BUY','STPFill',0)
                print('stop loss of short put option is executing')
                #closing a position
                close_position(shortlist_option,'short_put_option')
  
   
                first_trade_flag=5
                shortlist_option['first_trade_flag']=5
                store(shortlist_option)
   
    elif first_trade_flag==5:   
         print('first flag is 5') 

    if dt.datetime.now()>dt.datetime(current_time.year,current_time.month,current_time.day,end_hour,end_min):
           
            close_all_position()
    
            sys.exit()

