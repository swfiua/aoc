
from collections import Counter

valid = 0

for row in open('two.csv').read().split('\n'):
    fields = row.split()

    if not fields:
        continue

    minn, maxx = [int(x) for x in fields[0].split('-')]
    char = fields[1][0]

    password = fields[2]

    counts = Counter(password)

    if minn > 0 and char not in counts:
        print(minn, maxx, char, password, '***')
        continue

    count = counts[char]
    
    if minn <= count and count <= maxx:
        print(minn, maxx, count, char, password)
        valid += 1

print(valid)
