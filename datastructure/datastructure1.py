#list are mutable
l1=[22,33,44,55,'trading',55]

print(l1[0])
print(l1[-3:-1])

#string immutable
s1='hello'

print(s1[0])
print(s1[2:4])

print(l1[-1])

#changing value at index
l1[1]=99
print(l1)


#adding new elem in list
l1.append(87)
print(l1)

l1.insert(1,77)
print(l1)

#remove elem from list
l1.remove(55)
l1.remove(55)
print(l1)

v=l1.pop()
print(l1)
print(v)
