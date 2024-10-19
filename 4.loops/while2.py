






stock_prices={'amzn':400,'tsla':200,'goog':700,'nifty':1000}
portfolio={}
total=0
while True:
    name=input('enter the stock name (press Q to quit)')
    if name.upper()=='Q':
        print('stoping the program')
        break
    if name=='goog':
        print('you cannot trade this stock try something else')
        continue
    
    found=stock_prices.get(name)
    if found:
        portfolio.update({name:found})
        total=total+found
    else:
        print('invalid name')
print(portfolio)

print('total port is ',total)