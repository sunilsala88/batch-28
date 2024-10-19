






stock_prices={'amzn':400,'nvda':50000,'tsla':200,'goog':700,'nifty':1000}
portfolio={}
total=0

# while True:
#     name=input('enter the stock name (press Q to quit)')
#     if name.upper()=='Q':
#         print('stoping the program')
#         break
#     if name=='goog':
#         print('you cannot trade this stock try something else')
#         continue
    
#     found=stock_prices.get(name)
#     if found:
#         portfolio.update({name:found})
#         total=total+found
#     else:
#         print('invalid name')
# print(portfolio)

# print('total port is ',total)

max=0
name=0
# for i,j in stock_prices.items():
#     if j>max:
#         max=j
#         name=i
# print(max,name)

lkey=list(stock_prices.keys())
i=0
while True:
    
    if i==len(lkey):
        break
    k=lkey[i]
    v=stock_prices.get(k)
    if v>max:
        max=v
        name=k
    i=i+1

print(max,name)    

string1="hello"
l=len(string1)
print(l)
print(list(range(-1,((l+1)*(-1)),-1)))

print(list(range(-1,-6,-1)))
#"olleh"
ans=""
for i in range(-1,((l+1)*(-1)),-1):
    print(i)
    ans=ans+string1[i]
print(ans)

ans2=""
for i in string1:
    ans2=i+ans2
print(ans2)

numbers=[22,33,44,55]
ans2=[]
for i in range(-1,((len(numbers)+1)*(-1)),-1):
    ans2.append(numbers[i])
print(ans2)

ans3=[]
for i in numbers:
    ans3.insert(0,i)
print(ans3)