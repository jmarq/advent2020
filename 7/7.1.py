import networkx as nx

infile = open("input.txt", 'r')
rules = infile.read().strip().split("\n")

def parse_rule(line):
    color_name, contents = line.split(" bags contain ")
    # remove period
    contents = contents[:-1]
    contents = contents.replace("no other", "")
    contents = contents.replace(" bags", " bag")
    contents = contents.replace(" bag", "")
    # split by comma
    contents = contents.split(", ")
    result_contents = []
    for c in contents:
        if not c:
            continue
        # get the number/name
        split = c.split(" ",1)
        count = int(split[0])
        name= split[1]
        result_contents.append((name,count))
    return (color_name, result_contents)

    
rules = list(map(parse_rule, rules))

graph = nx.DiGraph()

for rule in rules:
    parent_name = rule[0]
    contents = rule[1]
    for c in contents:
        content_name = c[0]
        content_count = c[1]
        graph.add_edge(parent_name, content_name, weight=content_count)

results = 0
for node in graph.nodes:
    if "shiny gold" in nx.descendants(graph, node):
        results += 1
print(results)