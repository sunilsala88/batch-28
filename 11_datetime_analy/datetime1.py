#datetime 

# import datetime 
import datetime as dt
# from datetime import datetime
import time

dt1=dt.datetime(2024,11,24,18,25,5)
print(dt1)

d1=dt.date(2024,11,11)
t1=dt.time(12,15,15)

print(d1)
print(t1)

# def main():
#     print('inside main')

# while True:
#     ct=dt.datetime.now()
#     print(ct)
#     if ct.second==1 and ct.minute in range(0,60,5) :
#         main()
    # time.sleep(1)
u1=dt.timedelta(weeks=1)
print(dt1-u1)

#problem get me all thursday of this year
print(dt1.weekday())
#mon 0
#tue 1
#wed 2
#thu 3
#sun 6

# thursdays=[]
# current_day=dt.datetime(2024,1,1)
# while True:
#     if current_day.year==2025:
#         break
#     current_day=current_day+dt.timedelta(days=1)
#     if current_day.weekday()==6:
#         thursdays.append(current_day)

# print(thursdays)


#epoch to datetime
e1=1732454393
a1=dt.datetime.fromtimestamp(e1)
print(a1)

#datetime to epoch
print(dt1)
e2=dt1.timestamp()
print(e2)

#string to datetime
d1='2024-30-Dec-11-35-40'
f="%Y-%d-%b-%H-%M-%S"
dt5=dt.datetime.strptime(d1,f)
print(dt5)

#datetime to string
s1=dt5.strftime('%Y-%b000%H')
print(s1)

#get me epoch time for this string
s3='2 April 2018'
f="%d %B %Y"
dt6=dt.datetime.strptime(s3,f)
print(dt6)
e5=dt6.timestamp()
print(e5)