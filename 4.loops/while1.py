


# number=0
# sum=0
# while True:
#     if number==100:
#         break
#     number=number+1
#     if number%2==0:
#         print(number)
#         sum+=number
# print(sum)


l=[0,1]
num1=l[0]
num2=l[1]
print(num1)
print(num2)
count=len(l)
while True:
    if count==20:
        break
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3
    count=count+1
    