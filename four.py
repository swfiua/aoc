

passports = open('four.csv').readlines()


def check(data, required=None):

    required = required or set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    keys = set(data.keys())
    #print(keys, required)
    for x in required:
        if x not in keys:
            #print(x, keys)
            return False

    return True

def bad_year(year, start, end):

    year = int(year)
    if year < start or year > end:
        return True
    return False

def bad_height(value):

    units = value[-2:]
    #print(units)

    if units not in ['cm', 'in']: return True
    height = int(value[:-2])

    if units == 'in':
        if height < 59 or height > 76: return True
    if height < 150 or height > 193: return True

    return False

def bad_id(pid):
    return len(pid) != 9

def bad_hair(value):

    if len(value) != 7: return True

    if value[0] != '#': return True

    for c in value[1:]:
        if c not in '0123456789abcdef': return True

    return False
        

def check2(data):

    eyes = set('amb blu brn gry grn hzl oth'.split())
    for key, value in data.items():
        if key == 'byr':
            if bad_year(value, 1920, 2020):
                return False
        if key == 'hcl' and bad_hair(value): return False
        if key == 'iyr' and bad_year(value, 2010, 2020): return False
        if key == 'eyr' and bad_year(value, 2020, 2030): return False
        if key == 'hgt' and bad_height(value): return False
        if key == 'ecl' and value not in eyes: return False
        if key == 'pid' and bad_id(value): return False

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
    magic = 0
    passport = []
    total = 0
    for row in passports:
        if not row.strip():
            if passport:
                total += 1
                fields = get_fields(passport)
                if check(fields):
                    good += 1
                    if check2(fields):
                        magic += 1
                    else:
                        print(passport)
            passport = []
        else:
            passport.append(row)

    return good, magic, total


print(parse(passports))
