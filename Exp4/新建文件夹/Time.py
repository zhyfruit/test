class Time():
    def __init__(self, h = 0, m = 0, s = 0):
    #构造时、分、秒
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __str__(self):
        #以字符串形式显示时间
        return('%02d:%02d:%02d' % (self.__hour, self.__minute, self.__second))
    
    def __add__(self, n):
        #两个时间相加
        result = self.time2int() + n.time2int()
        #将时间都转化为以s为单位并相加
        r = Time()
        r.__hour = result / 3600 % 24
        r.__minute = result / 60 % 60
        r.__second = result % 60   
        print('the result of a + b is', r)       

    def time2int(self):
        #将时间对象转化为秒数
        result = (self.__hour * 60 + self.__minute)*60 + self.__second
        return result

    def printtime(self):
        #打印时间
        print('%02d:%02d:%02d' % (self.__hour, self.__minute, self.__second))
        return

    def isafter(self, n):
        #判断时间的迟早
        r1 = self.time2int()
        r2 = n.time2int()
        if r1 < r2:
            print('the former is earlier')
        elif r1 == r2:
            print('the same')
        else:
            print('the latter is earlier')
        return

    def increment(self, n):
        #n秒过后是几点
        r = self.time2int() + n
        result = Time()
        result.__hour = int(r / 3600 % 24)
        result.__minute = int((r - 3600 * result.__hour)/ 60 % 60)
        result.__second = r % 60
        print('after %d seconds is'%n,result)

    def isvalid(self):
        #判断时间是否是有效时间
        if self.__hour < 24 and self.__minute <= 60 and self.__second <= 60:
            print('is valid!')
            return
        else:
            print('notvalid')
            return
if __name__ == '__main__':
    import random
    r = Time(random.randint(0,24), random.randint(0,60), random.randint(0,60))
    print(r)
    s = Time(random.randint(0,24), random.randint(0,60), random.randint(0,60))
    s.printtime()
    r.isafter(s)
    t=Time(23, 59, 59)
    t.increment(20)
    w = Time(24, 70,70)
    w.isvalid()
    r+s

