from functools import reduce

infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")

print(len(lines))

lines = list(map(int,lines))
lines.sort()
print(lines)


initial_counts = [0,1,0] # 0 1s, 1 3(the one at the end), and the first charger is 0
def jump_reducer(accumulated_counts, current):
    #accumulated counts is (1count, 3count, prev)
    diff = current - accumulated_counts[2]
    if diff not in [1,2,3]:
        raise Exception("gap too big, what's up?")
    if diff == 1:
        accumulated_counts[0] += 1
    elif diff == 3:
        accumulated_counts[1] += 1
    accumulated_counts[2] = current
    return accumulated_counts

results = reduce(jump_reducer,lines,initial_counts)
print(results[0]*results[1])
