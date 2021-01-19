infile = open("input.txt", 'r')
groups = infile.read().strip().split("\n\n")

sum = 0
for group in groups:
    intersection = set(list('abcdefghijklmnopqrstuvwxyz'))
    members = group.split("\n")
    for member in members:
        intersection = intersection.intersection(set(list(member)))
    sum += len(intersection)

print(sum)