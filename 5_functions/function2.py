


# char1=55
# word=[57,66,77,88]
# t=char1 in word
# print(t)


# l=len('hello')
# print(l)


def something(x,y,z)->None:
    print(x,y,z)
    

something(y=30,z=20,x=10)


def calculate(list1,list2):
    print(list1,list2)

customer=[6,7,8]
prices=[6,7,5]
calculate(list2=customer,list1=prices)



def square(x):

    return x**2

def sum_of_square(list2):
    """calcualte square"""
    total=0
    for i in list2:
        total=total+square(i)

    return total

t=sum_of_square([1,2,3])
print(t)


#positionl argument
#default argument
#keyword argument



#difficult
#first 50 prime numbers

def is_prime(number):
    for i in range(2,number):
        rem=number%i
        if rem==0:
            return False
    return True

def get_list_of_primes(number1):
    list_of_primes=[]
    count=0
    number=1
    while True:
        # if len(list_of_primes)==1000:
        if count==number1:
            break
        if is_prime(number):
            list_of_primes.append(number)
            count=count+1
        number=number+1
    return (list_of_primes)

l=get_list_of_primes(10)
print(l)



initial_invest=1000
final=2*initial_invest
current_inv=initial_invest
interest=0.08
year=0
while True:
    if current_inv>=final:
        break
    current_inv=current_inv+(interest*current_inv)
    year=year+1

print(year)