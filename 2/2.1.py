infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")


def get_letter_range(line):
    rule_half = line.split(":")[0]
    letter = rule_half[-1]
    range_string = rule_half.split(" ")[0]
    minimum, maximum = range_string.split("-")
    minimum = int(minimum)
    maximum = int(maximum)
    return {
        "letter": letter,
        "min": minimum,
        "max": maximum
    }


def count_letter(letter, s):
    letters = list(s)
    count = len(list(filter(lambda l: l == letter, letters)))
    return count


def get_password(line):
    password_half = line.split(": ")[1]
    return password_half


def check_rule(rule, s):
    actual = count_letter(rule['letter'], s)
    return actual >= rule['min'] and actual <= rule['max']


def validate_line(line):
    rule = get_letter_range(line)
    password = get_password(line)
    return check_rule(rule, password)


if __name__ == "__main__":
    print(len(list(filter(validate_line, lines))))
