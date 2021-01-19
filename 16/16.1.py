import re

class TicketScanner():
    def __init__(self):
        self.rules = {}
        self.offending_values = []
    
    def add_rule(self,rule_line):
        rule_regex = r"([\w\s]+): (\d+-\d+) or (\d+-\d+)"
        rule_matcher = re.compile(rule_regex)
        match = rule_matcher.match(rule_line)
        groups = match.groups()
        rule_name, range_1, range_2 = groups

        range_1_split = range_1.split("-")
        range_1 = set(range(int(range_1_split[0]), int(range_1_split[1])+1))

        range_2_split = range_2.split("-")
        range_2 = set(range(int(range_2_split[0]), int(range_2_split[1])+1))

        valid_nums = range_1.union(range_2)
        self.rules[rule_name] = valid_nums

    def valid_for_any_rule(self, value):
        for valid_values in self.rules.values():
            if value in valid_values:
                return True
        return False

    def check_ticket(self, ticket_line):
        values = ticket_line.strip().split(",")
        values = list(map(int, values))
        for value in values:
            if not self.valid_for_any_rule(value):
                self.offending_values.append(value)
    
    def ticket_scanning_error_rate(self):
        return sum(self.offending_values)


if __name__ == "__main__":
    infile = open("input.txt", 'r')
    sections = infile.read().strip().split("\n\n")

    rules, your_ticket, nearby_tickets = sections

    scanner = TicketScanner()
    for rule in rules.strip().split("\n"):
        scanner.add_rule(rule)

    for ticket in nearby_tickets.strip().split("\n")[1:]:
        scanner.check_ticket(ticket)

    print(scanner.ticket_scanning_error_rate())

    
