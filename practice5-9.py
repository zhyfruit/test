def maxnum(lst):
    return (max(lst),sum(lst))
x=input("输入一个包含若干整数的列表：")
x=eval(x)
print(maxnum(x))
