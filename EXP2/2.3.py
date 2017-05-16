import random
from collections import Counter
cnt = Counter()
aList=[random.randint(1,100) for i in range(1000)]
for digit in aList:
    cnt[digit] += 1
print(cnt)
