aDict={'a':1,'b':2,'c':3,'d':4,'e':5}
x=input("请用户输入一个字典的键:")
print(aDict.get(x) if x in aDict else "您输入的键不存在！")
