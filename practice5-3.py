def demo(s):
    capital=little=digit=other=0
    for i in s:
        if(i<='z' and i>='a'):
            little+=1
        elif(i<='Z' and i>='A'):
            capital+=1
        elif(i>='0' and i<='9'):
            digit+=1
        else:
            other+=1
    return (capital,little,digit,other)

x=input("请输入一个字符串：")
print(demo(x))
