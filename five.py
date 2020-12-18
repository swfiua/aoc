
data = open('five.csv').readlines()

top = 0
values = set()
for item in data:

    row = 0
    for char in item[:7]:
        row *= 2
        if char == 'B':
            row += 1

    seat = 0
    for char in item[7:10]:
        seat *= 2
        if char == 'R':
            seat += 1
    
    value = (row * 8) + seat
    #print(value, len(item))

    if value > top:
        print(item, row, seat, value)
        top = value
    values.add(value)
print(top)


last = 0

start = min(values)
end = max(values)
print(start, end)

last = 0
for value in sorted(values):
    if 2 == value - last:
        print(value, value-last)
    last = value

for value in range(start, end):

    if value in values:
        # not mine
        continue
    #print(value)
    prev = value - 1
    post = value + 1
    if prev in values and post in values:
        print(value, '*****')
