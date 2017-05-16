x=input("请用户输入一个小于1000的整数：")
x=eval(x)
print(x,'=')
for i in range(2,x,1):
    if(x%i==0):
        print(i,'*')
        x=x/i
    for j in range(2,i,1):
        if(x%j==0):
            print(j,'*')
            x=x/j
