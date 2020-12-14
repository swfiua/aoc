
data = open('one.csv').read()

numbers = [int(x) for x in data.split('\n') if x.strip()]

print(len(numbers), numbers[0], numbers[-1])

for x in numbers:
    for y in numbers:
        if 2020 == x + y:
            print(x, y, x*y)

    
