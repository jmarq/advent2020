infile = open("input.txt", 'r')
rules = infile.read().strip().split("\n")
count = len(rules)
# acc jmp nop

cur = 0
seen = set()
total = 0
done = False
swap_tries = set()
swapped_this_time = False
failed_tries = 0
total_steps = 0

while cur not in seen:
    total_steps += 1
    line = rules[cur]
    action, num = line.split(" ")
    num = int(num)
    seen.add(cur)
    if action == "acc":
        total += num
        cur += 1
    elif action == "nop":
        if not swapped_this_time and cur not in swap_tries:
            swap_tries.add(cur)
            cur += num
            swapped_this_time = True
        else:
            cur += 1
    elif action == "jmp":
        if not swapped_this_time and cur not in swap_tries:
            swap_tries.add(cur)
            cur += 1
            swapped_this_time = True
        else:
            cur += num

    if cur in seen:
        # reset everything except for swap_tries
        total = 0
        seen = set()
        cur = 0
        swapped_this_time = False
        failed_tries += 1
    elif cur == count:
        print(total)
        print(failed_tries)
        print(total_steps)
        break

  


