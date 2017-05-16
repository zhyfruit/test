import random
aList=[random.randint(1,100) for i in range(20)]
print(aList)
bList=aList[::2]
bList.sort(reverse=True)
aList[::2]=bList
print(aList)
