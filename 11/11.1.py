infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")

matrix = list(map(list,lines))


def get_adjacent(row,col, matrix):
    results = []
    last_column_in_row = len(matrix[row]) - 1
    first_column_in_row = 0
    last_row = len(matrix) - 1
    first_row = 0

    if row != first_row:
        if col != first_column_in_row:
            # upper-left
            results.append(matrix[row-1][col-1])
        # directly above
        results.append(matrix[row-1][col])
        if col != last_column_in_row:
            #upper-right
            results.append(matrix[row-1][col+1])
    if col != first_column_in_row:
        # left
        results.append(matrix[row][col-1])
    if col != last_column_in_row:
        # right
        results.append(matrix[row][col+1])
    if row != last_row:
        if col != first_column_in_row:
            # lower-left
            results.append(matrix[row+1][col-1])
        # directly below
        results.append(matrix[row+1][col])
        if col != last_column_in_row:
            #lower-right
            results.append(matrix[row+1][col+1])
    return results

def next_state(current_state, adjacents):
    if current_state == "L":
        # currently empty. if there are no occupied seats adjacent, it becomes full.
        if "#" not in adjacents:
            return "#"
        pass
    elif current_state == "#":
        # currently filled. if there are four or more filled adjacent, it becomes empty.
        adjacents_filled = list(filter(lambda s: s == "#", adjacents))
        num_filled = len(adjacents_filled)
        if num_filled >= 4:
            return "L"
        pass
    elif current_state == ".":
        # floor never changes
        pass
    return current_state

def step(matrix):
    new_matrix = [row[:] for row in matrix]
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[0])):
            current = matrix[row][col]
            adjacents = get_adjacent(row,col,matrix)
            new_state = next_state(current, adjacents)
            new_matrix[row][col] = new_state
    return new_matrix

def num_filled(matrix):
    flattened = []
    for row in matrix:
        flattened += row
    filled = list(filter(lambda s: s=="#", flattened))
    return len(filled)

while True:
    stepped = step(matrix)
    if stepped == matrix:
        filled = num_filled(matrix)
        print(filled)
        break
    matrix = stepped
    



    