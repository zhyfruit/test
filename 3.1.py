x=input("请用户输入一个四位整数作为年份：")
x=eval(x)
if(x%400==0 or (x%4==0 and x%100!=0)):
    print(x, "是闰年。")
else:
    print(x,"不是闰年。")
