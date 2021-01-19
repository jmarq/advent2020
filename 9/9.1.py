from collections import deque

infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")

lines = list(map(int,lines))

# hmmm how to store the available sums?
#  we need to be able to remove the sums for the departing member of the list
#    as the "window" slides

# the numbers
current_window = deque()

#the sums
current_window_sums = deque()

for i in range(0, 25):
    sums_with_previous = deque()
    current_number = lines[i]
    for num in current_window:
        if num == current_number:
            sums_with_previous.append("x")
        else:
            sums_with_previous.append(current_number + num)
    current_window.append(current_number)
    current_window_sums.append(sums_with_previous)

for i in range(25,len(lines)):
    current_number = lines[i]
    previous_sums = []
    for d in current_window_sums:
        for num in d:
            previous_sums.append(num)
    if current_number not in previous_sums:
        print(current_number)
        break

    # start shifting, remove the first, and all the sums for it
    current_window.popleft()
    current_window_sums.popleft()
    for d in current_window_sums:
        d.popleft()

    sums_with_previous = deque()
    current_number = lines[i]
    for num in current_window:
        if num == current_number:
            sums_with_previous.append("x")
        else:
            sums_with_previous.append(current_number + num)
    current_window.append(current_number)
    current_window_sums.append(sums_with_previous)
    








