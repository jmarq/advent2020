from collections import deque

desired_sum = 70639851

infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")

lines = list(map(int,lines))

current_range = deque()


for start in range(0, len(lines)):
    range_length = 1
    range_sum = lines[start]
    while range_sum < desired_sum:
        range_sum += lines[start+range_length]
        range_length += 1
    if range_sum == desired_sum:
        sum_range = lines[start:start+range_length]
        print(min(sum_range) + max(sum_range))
        break






