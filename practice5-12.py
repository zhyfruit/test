def Sorted(lst):
    t=lst[::]
    r=[]
    while t:
        mint=min(t)
        r.append(mint)
        t.remove(mint)
    return r
x=input("请输入一个包含若干数据的列表：")
x=eval(x)
print(Sorted(x))
print(x)
