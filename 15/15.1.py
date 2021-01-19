from collections import deque

starting_numbers = [15,12,0,14,3,1]

turns_for_numbers = {}

for i in range(0,len(starting_numbers)):
    num = starting_numbers[i]
    if num not in turns_for_numbers:
        turns_for_numbers[num] = deque([i], maxlen=2)
    else:
        turns_for_numbers[num].append(i)

numbers = [num for num in starting_numbers]
turn = 6
prev_num = numbers[turn-1]
while turn < 30000000:
    new_number = 0
    if prev_num in turns_for_numbers:
        previous_utterances = turns_for_numbers[prev_num]
        if len(previous_utterances) > 1:
            new_number = previous_utterances[1] - previous_utterances[0]
    # numbers.append(new_number)
    if new_number not in turns_for_numbers:
        turns_for_numbers[new_number] = deque([turn], maxlen=2)
    else:
        turns_for_numbers[new_number].append(turn)
    turn += 1
    prev_num = new_number

print(prev_num)
