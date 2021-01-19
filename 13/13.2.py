infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")

trains = lines[1].split(",")
#trains = "17,x,13,19".split(",")
trains_with_offsets = []
for i in range(0,len(trains)):
    train = trains[i]
    if train != 'x':
        trains_with_offsets.append((i,int(train)))

print(trains_with_offsets)

current_step_size = trains_with_offsets[0][1]

num_trains = len(trains_with_offsets)
current_train = 1
i=0
for offset,train in trains_with_offsets[1:]:
    print("stepping by")
    print(current_step_size)
    print("train: "+str(train))
    found = []
    is_final_train = current_train == num_trains - 1
    if is_final_train:
        num_needed = 1
    else:
        num_needed = 2
    while len(found) < num_needed:
        if (i+offset) % train == 0:
            found.append(i)
            if is_final_train:
                print("DONE")
                print(i)
                break
        i += current_step_size
    if not is_final_train:
        print("found:")
        print(found)
        current_step_size = found[1] - found[0]
        current_train += 1
        i = found[0]

    