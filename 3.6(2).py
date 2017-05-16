x=input("请用户输入一个小于1000的整数：")
x=eval(x)
t=x
i=2
result=[]
while True:
    if t==1:
        break
    if t%i==0:
        result.append(i)
        t=t/i
    else:
        i+=1
print(x,'=','*'.join(map(str,result)))
