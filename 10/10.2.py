from functools import reduce
import networkx as nx

infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")
lines = list(map(int,lines))
lines.sort()
print(lines)

graph = nx.DiGraph()

highest_joltage = max(lines)

for i in range(0, highest_joltage):
    graph.add_edge(i, i+1)
    graph.add_edge(i, i+2)
    graph.add_edge(i, i+3)

#graph = graph.reverse()

graph = graph.subgraph([0,*lines])

# memoize the calls because the recursion will have a TON of duplicate calls
cache = {}

def ways_to_get_there(node, graph, cache):
    # check memo
    if node in cache:
        return cache[node]
    # check the possible previous steps
    predecessors = list(graph.predecessors(node))
    if len(predecessors) == 0:
        # base case. the starting point
        result = 1
    else:
        # add up the possible ways to get to each possible previous step
        count = 0
        for p in predecessors:
            count += ways_to_get_there(p, graph, cache)
        result = count
    # cache the result for next check of this node
    cache[node] = result
    return result

# how many ways to get to the last step?
print(ways_to_get_there(highest_joltage, graph, cache))