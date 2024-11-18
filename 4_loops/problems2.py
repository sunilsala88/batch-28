
# number= [+10, -20, +15, +30, -5]
# count=0
# for elem in number:
#     if elem>0:
#         count=count+1
# print(count)

# l1=[1,2,3]
# l2=[4,5,6]

# total_all=0
# for i in range(len(l1)):
#     total_all=total_all+(l1[i]*l2[i])
#     print(l1[i],l2[i])
# print(total_all)



returns=[0.02, -0.01, 0.03, 0.04,0.05, -0.02, 0.03,0.03, 0.04,0.05]
month_count=0
max=0
for ret in returns:
    if ret>0:
        month_count=month_count+1
        # month_count+=1
    else:
        month_count=0

    if max<month_count:
        max=month_count
print(max)
    

