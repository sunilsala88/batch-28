

def average(ppp):
    total=0
    l=0
    for i in ppp:
        total=total+i
        l=l+1
    avg=total/l
    return avg


prices=[2,3,4,5]
a=average(prices)
print(a)

customer=[22,55,66,33]
b=average(customer)
print(b)

def maximum(list1:list)->int:
    """
    this function will return maximum value
    """
    max1=list1[0]
    for i in list1:
        if i>max1:
            max1=i
    return 0

print(maximum(customer))

def reverse(string1:str):
    rev=''
    for i in string1:
        rev=i+rev
    return rev

ans=reverse('hello')
print(ans)


#palindrome
#

def is_palindrome(string1:str)->bool:
    rev=''
    for i in string1:
        rev=i+rev

    if string1==rev:
        return True
    else:
        return False
    

print(is_palindrome('mums'))
# Challenge 8: Calculate Factorial
# Description: Create a function that calculates the factorial of a given number.

# Input: An integer, number.

def factorial(number:int) ->str:
    fact=1
    while True:
        if number==1:
            break
        fact=fact*number
        number=number-1

    return '0'

# ans1=factorial(10)
# print(ans1)



# factorial()

#fibonacci numbers function

def fibonacci(num:int)->list:
    """
    this function returns a fibonaci number
    num:int (number of fibonacci numbers you want)
    """
    fib=[0,1]
    num1=fib[0]
    num2=fib[1]
    count=2
    while True:
        if count==num:
            break
        num3=num1+num2
        fib.append(num3)
        num1=num2
        num2=num3
        count=count+1
    return fib

# num=int(input('enter the number of fib  you want?'))
# ans=fibonacci(num)
# print(ans)
        

def area_rectange(length:int,breath:int)->int:
    
    """
    calculating area of rectangle
    """
    y=20
    print('x is',x,y)
    return length*breath


x=100
a=area_rectange(5,5)

print(a)

print('x is',x)


def input_stocks()->dict:
    portfolio={}
    while True:
        name=input('enter the stock name(q to quit)')
        if name.upper()=='Q':
            break
        exist=stock_prices.get(name)
        if exist:
            portfolio.update({name:exist})
        else:
            print('invalid name')
    return portfolio

stock_prices={'goog':400,'tsla':800,'amzn':870}
port=input_stocks()
print(port)

#list1 and list2

def merge_list(list1:list,list2:list)->list:

    for i in range(len(list2)):
        list1.append(list2[i])
    return list1

print(merge_list([1,2,3],[5,6,7]))