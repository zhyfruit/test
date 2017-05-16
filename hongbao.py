import random
def hongbao(total,num):
    total=total*100
    each=[]
    already=0
    for i in range(1,num):
        t=random.randint(1,(total-already)-(num-i))
        each.append(t)
        already=already+t
    each.append(total-already)
    for i in range(len(each)):
        each[i]=each[i]/100    
    return each
if __name__=='__main__':
    total=5
    num=5
    for i in range(30):
        each=hongbao(total,num)
        print(each)
