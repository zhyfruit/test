def Sum(lst):
    s=0
    for i in lst:
        s+=i
    return s
x=input("请输入一个包含若干个数据的列表：")
x=eval(x)
print(Sum(x))
