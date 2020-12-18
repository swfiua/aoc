

from block import blocks
from collections import Counter

groups = blocks('six.csv')
#groups = blocks('small.csv')

alpha = set('abcdefghijklmnopqrstuvwxyz')

result = 0
every = 0

for group in groups:
    c = Counter()
    
    for entry in group:
        c.update(entry)
        
    result += len(c)

    n = len(group)
    for k, v in c.items():
        if v == n:
            print(k, v)
            every += 1
    print(result, every)
print(result, every) 
