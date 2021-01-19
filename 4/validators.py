import re

#used for validating fields for 4.2

def byr(val):
    # four digits; at least 1920 and at most 2002.
    try:
        year = int(val)
        return len(val) == 4 and year >= 1920 and year <=2002
    except Exception as err:
        print(err)
        return False


def iyr(val):
    # four digits; at least 2010 and at most 2020.
    try:
        year = int(val)
        return len(val) == 4 and year >= 2010 and year <=2020
    except Exception as err:
        print(err)
        return False


def eyr(val):
    # four digits; at least 2020 and at most 2030.
    try:
        year = int(val)
        return len(val) == 4 and year >= 2020 and year <=2030
    except Exception as err:
        print(err)
        return False


def hgt(val):
    # a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    try:
        unit = val[-2:]
        magnitude = int(val[0:-2])
        if unit == "cm":
            return magnitude >= 150 and magnitude <= 193
        elif unit == "in":
            return magnitude >= 59 and magnitude <= 76
        else:
            return False
    except Exception as err:
        print(err)
        return False


def hcl(val):
    # a # followed by exactly six characters 0-9 or a-f.
    try:
        hair_regex = re.compile(r'#[0-9a-f]{6}$')
        return bool(hair_regex.match(val))
    except Exception as err:
        print(err)
        return False


def ecl(val):
    # exactly one of: amb blu brn gry grn hzl oth.
    try:
        valid_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return val in valid_values
    except Exception as err:
        print(err)
        return False


def pid(val):
    # a nine-digit number, including leading zeroes.
    try:
        pid_regex = re.compile(r'\d{9}$')
        return bool(pid_regex.match(val))
    except Exception as err:
        print(err)
        return False



def cid(val):
    # ignored, missing or not.
    return True
