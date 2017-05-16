from collections import Counter
cnt=Counter()

f1=open('xixi.txt','r') 
str1=[word.strip('"\'!,.').lower() for word in f1.read().split() if word.strip('"\'!,.').isalpha()]

for word in str1:
    cnt[word]+=1

print(cnt)
