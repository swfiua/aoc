

passports = open('four.csv').readlines()


def check(data, required=None):

    required = required or set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    keys = set(data.keys())
    #print(keys, required)
    for x in required:
        if x not in keys:
            print(x, keys)
            return False

    return True

def get_fields(data):

    result = {}
    for row in data:
        for item in row.split():
            key, value = item.split(':')
            result[key.strip()] = value.strip()

    return result
    

def parse(passports):

    good = 0
    passport = []
    total = 0
    for row in passports:
        if not row.strip():
            if passport:
                total += 1
                if check(get_fields(passport)):
                    good += 1
                else:
                    print(passport)
            passport = []
        else:
            passport.append(row)

    return good, total


print(parse(passports))
