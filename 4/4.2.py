import re
import validators

infile = open("input.txt", 'r')
passports = infile.read().strip().split("\n\n")
whitespace = re.compile(r'\s')

required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]
optional_fields = [
    'cid'
]


def validate_field(field_name, val):
    validator = getattr(validators, field_name)
    return validator(val)


def get_fields(passport_blob):
    fields = {}
    field_chunks = whitespace.split(passport_blob)
    for chunk in field_chunks:
        key, val = chunk.split(":")
        fields[key] = val
    return fields


def validate_fields(fields):
    for field in required_fields:
        if field not in fields:
            return False
        value = fields[field]
        if not validate_field(field, value):
            return False
    return True


def validate_blob(passport_blob):
    fields = get_fields(passport_blob)
    is_valid = validate_fields(fields)
    return is_valid


if __name__ == "__main__":
    valid_passports = list(filter(validate_blob, passports))
    print(len(valid_passports))
