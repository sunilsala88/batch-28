#split and join

l1=['abc','askjd','asdkfj']
ans1=' '.join(l1)
print(ans1)

s1='als,jdfl,kajs'
l2=s1.split(',')
print(l2)

#truthy and falsy value
#falsy values 0,False,[],{},"",()
a='hello'
print(a)
if a:
    print('inside if')
else:
    print('inside else')



stock_prices={'amzn':500,'tsla':900,'goog':900,99:100}
print(stock_prices)

v=stock_prices.get('nifty')

if v:
    print(v)
else:
    print('key doesnt exist')