import re
infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")


# line = "1 + (2 * 3) + (4 * (5 + 6))"
# line = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
# line = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
# line = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
#line = "1 + 2 * 3"
line = "1 + 2 * 3 + 4 * 5 + 6"

def process_chained_operators(line):
    line = process_addition(line)
    line = process_multiplication(line)
    return line

def process_addition(line):
    operation_re = re.compile(r"\d+ [\+] \d+")
    match = operation_re.search(line)
    while match:
        evaluated = perform_single_operation(match.group())
        line = line.replace(match.group(), evaluated,1)
        match = operation_re.search(line)
    return line

def process_multiplication(line):
    operation_re = re.compile(r"\d+ [\*] \d+")
    match = operation_re.search(line)
    while match:
        evaluated = perform_single_operation(match.group())
        line = line.replace(match.group(), evaluated,1)
        match = operation_re.search(line)
    return line


def perform_single_operation(op_string):
    evalualted = eval(op_string)
    return str(evalualted)


def evaluate_parens(line):
    simple_paren_re = re.compile(r"\(([\d\s\*\+]+)\)")
    found = simple_paren_re.search(line)
    while found:
        paren_string = found.group()
        expression_within = found.groups()[0]
        print(expression_within)
        evaluated = process_chained_operators(expression_within)
        line = line.replace(paren_string, evaluated, 1)
        found = simple_paren_re.search(line)
    return line

def evaluate_whole_line(line):
    line = "("+line+")"
    result = evaluate_parens(line)
    return result

#print(evaluate_whole_line(line))

total = 0
for problem in lines:
    result = int(evaluate_whole_line(problem))
    total += result
    # print(result)
print(total)

# print(evaluate_whole_line("2 * 2 + 3 + 2 * 2"))