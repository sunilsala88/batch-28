# l1=[5,6,7]

# #type 1->go through each elem of list
# total=0
# for elem in l1:
#     total=total+elem
# print(total)
# avg=total/len(l1)
# print(avg)

# #type 2-> run a piece of code for n times
# a='python'
# l2=[0,1,2,3,4,5,6,7,8,9]
# l3=list(range(100))
# print(l3)
# for i in range(100):
#     print(a)

# #type 3->go through each elem of list using its index
# prices=[666,777,888,33,99,78,99]
# indexes=[0,1,2,3,4]
# indexes=range(len(prices))
# for i in range(len(prices)):
#     print(prices[i])


# #problem 1
# r1=list(range(10))
# print(r1)

# r2=list(range(100,200))
# print(r2)

# r3=list(range(0,101,10))
# print(r3)

# # for i in r1:
# #     if i%2==0:
# #         print(i)

# even=list(range(0,101,2))
# print(even)
# total=0
# for i in even:
#     total=total+i
# print(total)


#type 4

d1={'amzn':100,'goog':200,'tsla':900}
# print(d1.keys())
# print(d1.values())
# print(d1.items())

sum=0
for i,j in d1.items():
    sum=sum+j
    #sum+=j

d1.update({'total':sum})
print(d1)
