
# stock_prices={'amzn':500,'tsla':900,'goog':900,99:100}
# print(stock_prices)

# #accessing new way
# print(stock_prices.get('nvda'))

# #accessing old way
# print(stock_prices['tsla'])
# print(stock_prices[99])

# #add  a new elem/update existing elem
# stock_prices.update({'tsla':990})
# print(stock_prices)

# #old way
# stock_prices['banknifty']=590
# print(stock_prices)

# #deleting a key value pair
# stock_prices.pop(99)
# print(stock_prices)

# #old way
# del stock_prices['amzn']
# print(stock_prices)

# #values keys items
# print(list(stock_prices.keys()))
# print(list(stock_prices.values()))
# print(list(stock_prices.items()))

#sets
s1={1,2,3,2}
print(s1)
print(type(s1))

s2=set([4,5,6,6,7])
print(s2)
print(type(s2))

s2.add(88)
print(s2)

s2.remove(6)
print(s2)

a=s2.pop()
print(a)
print(s2)

s2.pop()
print(s2)

