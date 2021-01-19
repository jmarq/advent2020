from functools import reduce

infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")

line_length = len(lines[0])
num_lines = len(lines)

def check_slope(h_speed, v_speed):
    trees = 0
    x_pos = 0
    y_pos = 0

    while y_pos < num_lines:
        is_tree = lines[y_pos][x_pos % line_length] == '#'
        if is_tree:
            trees += 1
        x_pos += h_speed
        y_pos += v_speed
    return trees

slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

if __name__ == "__main__":
    counts = map(lambda s: check_slope(s[0], s[1]), slopes)
    multiplied = reduce(lambda c,prev: c*prev, counts, 1)

    print(multiplied)
