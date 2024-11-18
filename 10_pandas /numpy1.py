import numpy as np

# l1=[1,2,3]
# np1=np.array(l1)

# print(l1)
# print(np1)

# print([1,2,3]+[4,5,6])
# print(np.array([1,2,3])*np.array([4,5,6]))


# print(np.ones(10))
# print(np.zeros(5))
# np3=np.arange(100,200,5)
# print(np3[0:3])
# print(np3[:])


l3=[ [1,2,3],[4,5,6],[7,8,9]]
print(l3)
np3=np.array(l3)
print(np3)

print(np3[[0,1,2],[0,1,2]])
print(np3[[0,1,2],[2,1,0]])


a1=np.arange(25,50).reshape(5,5)
print(a1)

print(a1[0,[2,3]])
print(a1[0,2:4])
print(a1[[2,3,4],2])
print(a1[2:5,2])

r1=np.random.randint(1,100,size=(3,3))
print(r1)