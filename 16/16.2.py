import re


class TicketScanner():
    def __init__(self):
        self.rules = {}
        self.possibility_sets = []

    def add_rule(self, rule_line):
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

    def initialize_possiblities(self):
        rule_names = list(self.rules.keys())
        self.possibility_sets = [set(rule_names)
                                 for i in range(len(rule_names))]

    def valid_for_any_rule(self, value):
        for valid_values in self.rules.values():
            if value in valid_values:
                return True
        return False

    def validate_ticket(self, ticket_line):
        values = ticket_line.strip().split(",")
        values = list(map(int, values))
        for value in values:
            if not self.valid_for_any_rule(value):
                return False
        return True

    def possible_rules_for_value(self, value):
        results = []
        for name, valid_values in self.rules.items():
            if value in valid_values:
                results.append(name)
        return set(results)

    def account_for_ticket(self, ticket_line):
        values = ticket_line.strip().split(",")
        values = list(map(int, values))
        for i in range(0, len(values)):
            previous_possibilities = self.possibility_sets[i]
            value = values[i]
            possible_rules = self.possible_rules_for_value(value)
            self.possibility_sets[i] = possible_rules.intersection(
                previous_possibilities)

    def collapse_possibilities(self):
        lengths = list(map(len, self.possibility_sets))
        while sum(lengths) > 20:
            for i in range(0, len(self.possibility_sets)):
                s = self.possibility_sets[i]
                if len(s) == 1:
                    val = list(s)[0]
                    for s2 in self.possibility_sets:
                        if s != s2 and val in s2:
                            s2.remove(val)
            lengths = list(map(len, self.possibility_sets))

    def get_departure_indexes(self):
        results = []
        for index, ps in enumerate(self.possibility_sets):
            if "departure" in list(ps)[0]:
                results.append(index)
        return results


if __name__ == "__main__":
    infile = open("input.txt", 'r')
    sections = infile.read().strip().split("\n\n")

    rules, your_ticket, nearby_tickets = sections

    scanner = TicketScanner()
    for rule in rules.strip().split("\n"):
        scanner.add_rule(rule)
    scanner.initialize_possiblities()

    nearby_tickets = nearby_tickets.strip().split("\n")[1:]
    valid_tickets = list(filter(scanner.validate_ticket, nearby_tickets))
    for ticket in valid_tickets:
        scanner.account_for_ticket(ticket)

    scanner.collapse_possibilities()

    departure_indexes = scanner.get_departure_indexes()

    your_ticket_values = your_ticket.split("\n")[1].strip().split(",")
    your_ticket_values = list(map(int, your_ticket_values))
    product = 1
    for index in departure_indexes:
        product *= your_ticket_values[index]
    print(product)
