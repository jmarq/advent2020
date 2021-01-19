infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")

line_length = len(lines[0])

horizontal_speed = 3

trees = 0
x_pos = 0
for line in lines:
    is_tree = line[x_pos % line_length] == '#'
    if is_tree:
        trees += 1
    x_pos += horizontal_speed

print(trees)
