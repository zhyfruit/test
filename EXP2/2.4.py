aList=input("请输入一个列表:")
aList=aList.strip("[]").split(',')
for i in range(len(aList)):
    aList[i]=int(aList[i])
x=input("请输入两个整数作为下标:")
a,b=x.split(',')
a=int(a)
b=int(b)
print(aList[a:b])
