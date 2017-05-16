import time

def rev_str_cnt(f):
    dic = {}
    cnt = 0
    lines = [i.strip('\n') for i in f.readlines()]

    start= time.time()
    for line in lines:
        #line = line.strip('\n')
        if dic.get(line):
            dic[line] += 1
        else:
            dic[line] = 1
        if dic.get(line[::-1]):
            cnt += dic[line[::-1]]
        #    print( line, line[::-1], " ")
    print(time.time() - start)
    return cnt
if __name__ == '__main__':
    fname = r'C:\spring17\pyexp2.4\words.txt'
    f = open(fname, 'r')
    print(rev_str_cnt(f))
