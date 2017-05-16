sum=0
aList=[i for i in range(100)]
bList=aList[1::2]
for digit in bList:
    sum=sum+digit
print(sum)
