import math
def IsPrime(n):
    m=int(math.sqrt(n))+1
    for i in range(2,m):
        if n%i==0:
            return False
    return True
x=input("请输入一个整数：")
x=eval(x)
if(IsPrime(x)):
    print(x,"是素数")
else:
    print(x,"不是素数")
    
