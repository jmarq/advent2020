infile = open("input.txt", 'r')
groups = infile.read().strip().split("\n\n")

sum = 0
for group in groups:
    group = group.replace("\n","")
    group = set(list(group))
    sum += len(group)

print(sum)