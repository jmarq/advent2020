infile = open('input.txt','r')
lines = infile.readlines()
numbers = list(map(lambda l: int(l.strip()), lines))
print(numbers)


seen = set()
result = None
for num in numbers:
    diff = 2020 - num
    if diff in seen:
        result = num * diff
        break
    seen.add(num)

print(result)
