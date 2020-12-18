

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

def bad_year(key, year, start, end):

    year = int(year)
    if year < start or year > end:
        print(key, year)
        return True
    return False

def bad_height(key, value):

    units = value[-2:]
    #print(units)

    if units not in ['cm', 'in']:
        print(key, value)
        return True

    height = int(value[:-2])

    if units == 'in':
        if height < 59 or height > 76:
            print(key, value)
            return True

    elif height < 150 or height > 193:
        print(key, value)
        return True

    return False

def bad_id(key, pid):

    result = len(pid) != 9

    if result:
        print(key, pid)

    return result
    

def bad_hair(key, value):

    result = False
    if len(value) != 7: result = True

    if value[0] != '#': result = True

    for c in value[1:]:
        if c not in '0123456789abcdef': result = True

    if result:
        print(key, value)
        
    return result
        

def check2(data):

    eyes = set('amb blu brn gry grn hzl oth'.split())
    for key, value in data.items():
        if key == 'byr' and bad_year(key, value, 1920, 2002): return False
        if key == 'iyr' and bad_year(key, value, 2010, 2020): return False
        if key == 'eyr' and bad_year(key, value, 2020, 2030): return False
        if key == 'hcl' and bad_hair(key, value): return False
        if key == 'hgt' and bad_height(key, value): return False
        if key == 'ecl' and value not in eyes: return False
        if key == 'pid' and bad_id(key, value): return False

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
                        print(len(fields))
            passport = []
        else:
            passport.append(row)

    return good, magic, total


print(parse(passports))
