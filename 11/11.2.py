infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")

matrix = list(map(list, lines))


UP_LEFT = [-1, -1]
UP = [-1, 0]
UP_RIGHT = [-1, 1]
LEFT = [0, -1]
RIGHT = [0, 1]
DOWN_LEFT = [1, -1]
DOWN = [1, 0]
DOWN_RIGHT = [1, 1]

DIRECTIONS = [UP_LEFT, UP, UP_RIGHT, LEFT, RIGHT, DOWN_LEFT, DOWN, DOWN_RIGHT]


def direction_step(coords, direction):
    result = [coords[0]+direction[0], coords[1]+direction[1]]
    return result

def get_first_seen(row, col, matrix, direction):
    cur = [row, col]
    while True:
        try:
            look_at_coords = direction_step(cur, direction)
            if -1 in look_at_coords:
                raise Exception
            seat = matrix[look_at_coords[0]][look_at_coords[1]]
            if seat != ".":
                return seat
            cur = look_at_coords
        except:
            return "."


def get_adjacent(row, col, matrix):
    results = []
    for direction in DIRECTIONS:
        results.append(get_first_seen(row, col, matrix, direction))
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
        if num_filled >= 5:
            return "L"
        pass
    elif current_state == ".":
        # floor never changes
        pass
    return current_state


def step(matrix):
    new_matrix = [row[:] for row in matrix]
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            current = matrix[row][col]
            adjacents = get_adjacent(row, col, matrix)
            new_state = next_state(current, adjacents)
            new_matrix[row][col] = new_state
    return new_matrix


def num_filled(matrix):
    flattened = []
    for row in matrix:
        flattened += row
    filled = list(filter(lambda s: s == "#", flattened))
    return len(filled)


while True:
    stepped = step(matrix)
    if stepped == matrix:
        filled = num_filled(matrix)
        print(filled)
        break
    matrix = stepped

# stepped = matrix
# stepped = step(stepped)
# for row in stepped:
#     print("".join(row))
# print("\n\n")
# stepped = step(stepped)
# for row in stepped:
#     print("".join(row))
