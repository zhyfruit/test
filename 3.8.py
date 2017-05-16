digits=(1,2,3,4)
result=[]
for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                if i!=j and j!=k and k!=l and l!=i and i!=k and j!=l:
                    digit=i*1000+j*100+k*10+l
                    result.append(digit)
import math
for x in result:
    m=math.ceil(math.sqrt(x)+1)
    for i in range(2,m):
        if x%i==0 and i<x:
            break
    else:
            print(x)
        
