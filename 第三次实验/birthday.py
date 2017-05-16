import random
import time
#对生日列表进行排序，并判断是否有同一天
def has_duplicates(t):
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False
#随机生成n个同学的生日，依次加入生日列表
def random_bdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t
#模拟统计结果有相同生日的模拟次数
def count_matches(students, samples):
    count = 0
    for i in range(samples):
        t = random_bdays(students)
        if has_duplicates(t):
            count += 1
    return count

num_students = input("请输入学生数：")
num_students = int(num_students)
num_simulations = 1000
p=0
start=time.time()
count = count_matches(num_students, num_simulations)
P=count  / 1000
print(time.time()-start)

print('在 %d 次模拟后' % num_simulations)
print('共有 %d 个学生参与模拟实验' % num_students)
print('共有 %d 次模拟中至少有两个学生生日在同一天' % count)
print('相同生日的概率估计为:%lf' % P)


