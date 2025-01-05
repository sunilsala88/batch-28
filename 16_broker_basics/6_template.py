import datetime as dt
import time



def main_strategy_code():
    print('we are running strategy ')



current_time=dt.datetime.now()
print(current_time)

start_hour,start_min=19,3
end_hour,end_min=19,6

start_time=dt.datetime(current_time.year,current_time.month,current_time.day,start_hour,start_min)
end_time=dt.datetime(current_time.year,current_time.month,current_time.day,end_hour,end_min)

print(start_time)
print(end_time)

while dt.datetime.now()<start_time:
    print(dt.datetime.now())
    time.sleep(1)
print('we have reached start time')



while True:
    if dt.datetime.now()>end_time:
        break
    ct=dt.datetime.now()
    print(ct)
    
    if ct.second==1: #and ct.minute in range(0,60,5):#[0,5,10,15..55]
        main_strategy_code()
    time.sleep(1)
print('strategy stopped')