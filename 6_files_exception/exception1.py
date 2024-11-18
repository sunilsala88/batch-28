#ZeroDivisionError
#ValueError


# try:
#     num1=int(input('enter number 1'))
#     num2=int(input('enter number 2'))

#     ans=num1/num2
#     print(ans)
# except Exception as e:
#     print(e)
#     print('something went wrong')

# print('this is important')


# list1=[44,55,667,90,88,7,8,9]
# while True:
#     try:
#         i=int(input('enter the index(-1 to break)'))
#         if i==-1:
#             break
#         print(list1[i])
#     except Exception as e:
#         print(e)
#         print('invalid input')
# print('closing all position')


try:
    num1=int(input('enter number 1'))
    num2=int(input('enter number 2'))

    ans=num1/num2
    print(ans)
except ZeroDivisionError as  e:
    print(e)
    print('you cannot type 0 as second number')
except ValueError as v:
    print(v)
    print('you cannot type alphabet')

print('this is important')