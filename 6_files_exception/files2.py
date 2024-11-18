
f=open('data.txt','r')
d=f.read()
list1=d.split('\n')
stock_prices={}
total=0
for item in list1:
    print(item)
    k,v=item.split(':')
    print(k,v)
    stock_prices.update({k:int(v)})
    total=total+int(v)
stock_prices.update({'total':total})

print(stock_prices)
f.close()

f=open('data.txt','a')
f.write(f'\ntotal:{total}')
f.close()