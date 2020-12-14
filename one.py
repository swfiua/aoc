
data = open('one.csv').read()

numbers = [int(x) for x in data.split('\n') if x.strip()]

for x in numbers:
    for y in numbers:
        for z in numbers:
            if 2020 == x + y + z:
                print(x, y, z, x * y * z)

    
