# #list are mutable
l1=[22,33,44,55,'trading',55]

# print(l1[0])
# print(l1[-3:-1])

# #string immutable
# s1='hello'

# print(s1[0])
# print(s1[2:4])

# print(l1[-1])

# #changing value at index
# l1[1]=99
# print(l1)

# l1[-2]=0
# print(l1)

# #adding new elem in list
l1.append(87)
print(l1)

# l1.insert(1,77)
# print(l1)

# #remove elem from list
# l1.remove(55)
# l1.remove(55)
# print(l1)

# v=l1.pop()
# print(l1)
# print(v)

# # l1.clear()
# t=l1.count(55)
# print(t)
# print(l1)
# a=l1.index(44)
# print(a)

# m1=[1,2,3]
# m2=[5,6,7]
# m1.extend(m2)
# print(m1)



s1='fessorPro'
a=s1.index('s')
print(a)
b=s1.upper()
print(b)
print(s1)
print(s1.lower())
print(s1.endswith('rr'))
print(s1.find('e'))

stocks=['a','b','v']
print('-'.join(stocks))

st1='alsdjf lajsdf jlk'
print(st1.split(' '))

string3='python'
a=string3.replace('o','a')
print(a)

st5='  aklsjdflas   '
print(st5.strip())


# list1=[66,77,88]
# del list1[0]
# print(list1)


t1=(55,66,77,'world')
print(t1)
t1.count(66)
print(t1.index(55))