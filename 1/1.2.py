infile = open('input.txt','r')
lines = infile.readlines()
numbers = list(map(lambda l: int(l.strip()), lines))
numbers.sort()
print(numbers)

def find_pair_for_sum(nums,total):
    seen = set()
    result = None
    for num in nums:
        if num > total:
            break
        diff = total - num
        if diff in seen:
            result = num * diff
            break
        seen.add(num)
    return result

result = None
for i in range(0,len(numbers)):
    diff = 2020 - numbers[i]
    found_pair = find_pair_for_sum(numbers[i+1:], diff)
    if found_pair:
        result = numbers[i] * found_pair
        break

print(result)
