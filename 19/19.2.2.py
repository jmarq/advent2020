import re

infile = open("input_with_loops.txt",'r')
rules_chunk, messages_chunk = infile.read().strip().split("\n\n")

rule_lines = rules_chunk.strip().split("\n")
message_lines = messages_chunk.strip().split("\n")

simple_rule_parser = re.compile(r"(\d+): (.*$)")
rule_lookup = {}
for rule in rule_lines:
    match = simple_rule_parser.match(rule)
    number = match.groups()[0]
    rule_body = match.groups()[1].replace("\"","")
    rule_lookup[number] = {
        'rule': rule_body.replace("\"",""),
        'regex': None if rule_body not in ["a", "b"] else rule_body
    }

print(rule_lookup)

# validator = re.compile(r"a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b$")

# lines = [
#     "ababbb",
#     "bababa",
#     "abbbab",
#     "aaabbb",
#     "aaaabbb"
# ]

# for line in lines:
#     if validator.match(line):
#         print(line)

# holy shit that worked?

# hmmm I wonder if it is feasible to make a similar regex to represent the entire problem?

# how to even start?

# 4 1 5 ---> concat the regex for each
# "a" + 1 5
#  1 --> ( 2 3 | 3 2)
#       2 ---> (4 4 | 5 5)
#           4 ---> a

# concat ANDs and (expanded|expanded) ORs

# 3: 4and5 OR 5and4
# 3: ab OR ba
# 3: (ab|ba)

recursive_calls = {}

def number_to_regex(number_string, caller="X"):
    #lookup number in ruleset
    
    rule_entry = rule_lookup[number_string]
    if rule_entry['regex']:
        return rule_entry['regex']

    rule_string = rule_entry['rule']

    if caller not in recursive_calls:
        recursive_calls[caller] = 1
    else:
        recursive_calls[caller] += 1
        print(caller)
        print(recursive_calls[caller])
    

    rules_to_or = rule_string.split(" | ")
    regexes_to_or = []
    for rule in rules_to_or:
        rules_to_and = rule.strip().split(" ")
        index_of_recursion = -1
        if (caller in rules_to_and):
            index_of_recursion = rules_to_and.index(caller)
            rules_to_and.remove(caller)
        regexes_to_and = []
        for a in rules_to_and:
            regexes_to_and.append(number_to_regex(a, number_string))
        # regexes_to_and = list(map(number_to_regex, rules_to_and))
        anded = "".join(regexes_to_and)
        if index_of_recursion != -1:
            regexes_to_and.insert(index_of_recursion, "("+anded+")*")
            anded = "".join(regexes_to_and)
        regexes_to_or.append(anded)
    if len(regexes_to_or) > 1:
        result = "("+"|".join(regexes_to_or)+")"
    else:
        result = regexes_to_or[0]
    rule_entry['regex'] = result
    return result


insane_validator_string = number_to_regex("0")+"$"
insane_validator = re.compile(insane_validator_string)

total = 0
for line in message_lines:
    if insane_validator.match(line):
        total += 1
print(total)
# print(insane_validator_string)

# regex_42 = number_to_regex("42")
# print(regex_42)