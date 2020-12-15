
from collections import Counter

valid = 0
valid2 = 0
valid3 = 0

for row in open('two.csv').read().split('\n'):
    fields = row.split()

    if not fields:
        continue

    minn, maxx = [int(x) for x in fields[0].split('-')]
    char = fields[1][0]

    password = fields[2]

    counts = Counter(password)

    schar = password[minn-1]
    echar = password[maxx-1]
    
    if schar == char or echar == char:
        valid3 += 1
        print(minn, maxx, char, schar, echar, password, '333')
        if echar != schar:
            print(minn, maxx, char, schar, echar, password, '***')
            valid2 += 1

    if minn > 0 and char not in counts:
        continue

    count = counts[char]
    
    if minn <= count and count <= maxx:
        #print(minn, maxx, count, char, password, '999')
        valid += 1

print(valid, valid2, valid3)
