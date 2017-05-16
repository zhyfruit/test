import random
aList=[random.randint(1,100) for i in range(50)]
print(aList) 
for j in range(len(aList)-1,-1,-1):
    if aList[j]%2!=0:
        del aList[j]
print(aList)
