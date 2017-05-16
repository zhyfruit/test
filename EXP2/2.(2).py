from math import sqrt
list1=[]
for i in range(2,100):
    for j in range(2,int(sqrt(i))+1):
        if i%j==0:
            break
    else:
        list1.append(i)
print(list1)

