
#writing data to txt file
# data='amzn'

# f=open('data.txt','w')
# f.write(data)
# f.close()


#appending data to txt file
# data='amzn'

# f=open('data.txt','a')
# f.write(data)
# f.close()


#read data from text
f=open('data.txt','r')
d=f.read()
print(d)
print(type(d))
f.close()