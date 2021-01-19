from collections import deque
from copy import deepcopy


def expand_space(space):
    #space being a 3d deque
    
    new_row_length = len(space[0][0]) + 2
    new_plane_height = len(space[0]) + 2
    # new_row = generate_new_row#["." for i in range(0,new_row_length)]

    for plane in space:
        for row in plane:
            row.append(".")
            row.appendleft(".")
        plane.append(generate_new_row(new_row_length))
        plane.appendleft(generate_new_row(new_row_length))
    space.append(generate_new_plane(new_row_length, new_plane_height))
    space.appendleft(generate_new_plane(new_row_length, new_plane_height))

            
def generate_new_row(width):
    new_row = ["." for i in range(0,width)]
    return deque(new_row)

def generate_new_plane(width, height):
    new_plane = deque(
        [generate_new_row(width) for i in range(0,height)]
    )
    return new_plane

def step(space):
    expand_space(space)
    new_space = deepcopy(space)
    for z in range(0, len(space)):
        for y in range(0,len(space[0])):
            for x in range(0,len(space[0][0])):
                current_val = space[z][y][x]
                active_neighbor_count = get_active_neighbor_count(space, z, y, x)
                # print("active neighbor count: "+str(active_neighbor_count))
                if current_val == "#":
                    if active_neighbor_count in [2,3]:
                        new_val = "#"
                    else:
                        new_val = "."
                elif current_val == ".":
                    if active_neighbor_count == 3:
                        new_val = "#"
                    else:
                        new_val = "."
                new_space[z][y][x] = new_val
    return new_space


def get_neighbor_indexes(z,y,x):
    result_coords = []
    for z2 in range(z-1, z+2):
        for y2 in range(y-1, y+2):
            for x2 in range(x-1, x+2):
                result_coords.append((z2,y2,x2))
    result_coords.remove((z,y,x))
    return result_coords

def get_neighbor_values(space, z,y,x):
    indexes = get_neighbor_indexes(z,y,x)
    results = []
    for index in indexes:
        try:
            if -1 in index:
                results.append(".")
            else:
                val = space[index[0]][index[1]][index[2]]
                results.append(val)
        except Exception as e:
            # print(e)
            results.append(".")
    return results

def get_active_neighbor_count(space, z,y,x):
    neighbor_values = get_neighbor_values(space, z, y, x)
    # print("neighbor values: "+str(neighbor_values))
    active_neighbors = list(filter(lambda s: s=="#", neighbor_values))
    return len(active_neighbors)
    
def count_actives(space):
    count = 0
    for z in range(0, len(space)):
        for y in range(0,len(space[0])):
            for x in range(0,len(space[0][0])):
                if space[z][y][x] == "#":
                    count += 1
    return count


infile = open("input.txt", 'r')
lines = infile.read().strip().split("\n")

list_lines = map(list,lines)
list_lines = map(deque, list_lines)
deque_of_rows = deque(list_lines)
space = deque([deque_of_rows])


print(len(space))
for i in range(0,6):
    space = step(space)
print(space)
print(count_actives(space))
