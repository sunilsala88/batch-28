#swap values of 2 var
a=10
b=20
# c=a
# a=b
# b=c
# print(a,b)

b,a=a,b
print(a,b)


#first 10 fib number
num1=0
num2=1

# num3=num1+num2
# num4=num3+num2
# ...
# num10=num9+num8

for i in range(8):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3)


prices=[2000, 3000, 1500, 4000, 2800]
high_price=prices[0]
for cp in prices:
    if cp>high_price:
        high_price=cp
    print(high_price)

print(high_price)

