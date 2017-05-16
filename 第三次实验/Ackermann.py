#https://en.wikipedia.org/wiki/Ackermann_function
import time
def Ack(m,n):
    if m==0:
        z=n+1
    elif m>0 and n==0:
        z=int(Ack(m-1,1))
    elif m>0 and n>0:
        z=int(Ack(m-1,Ack(m,n-1)))
    return z
start=time.time()
print(Ack(3,4))
print(time.time()-start)
