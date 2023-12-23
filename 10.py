# advent of code 2023 - day 10
# by bewu 22/12/2023
from sys import setrecursionlimit

setrecursionlimit(30000)

input_ = """.....
.S-7.
.|.|.
.L-J.
....."""
input_ = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
input_ = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
with open("input/10.txt", "r") as f:
    input_ = f.read()
# input_ = """|F--J
# LS--|
# .L--J"""

input_lines = [list(i) for i in input_.splitlines()]

width = len(input_lines[0])
height = len(input_lines)

distance_table = [ [None for _ in range(width)] for _ in range(height) ]

f = input_.replace("\n", "").find("S")
start_y = f // width
start_x = f - width*start_y

offset_north = [0, -1]
offset_south = [0, 1]
offset_east = [1, 0]
offset_west = [-1, 0]

def check(x, y, prev_x, prev_y, history, curr_distance=0, reverse=False):
    # if x == prev_x and y == prev_y: # going back
    #     return
    
    # print(f"check {x} {y} from ({prev_x} {prev_y})")
    history.append([x, y])
    global distance_table
        
    # if distance_table[y][x] != None:
    #     return
    if y == start_y and x == start_x and curr_distance > 0:
        return history
    
    curr_tile = input_lines[y][x]
    # print(curr_tile)
    
    distance_table[y][x] = min(curr_distance, distance_table[y][x] if distance_table[y][x] else 999999999)
    curr_distance += 1
    
    # print(curr_tile)

    offsets = []
    
    if curr_tile == "S": # go in all 4 directions
        offsets = [offset_north, offset_east, offset_south, offset_west]
        if reverse:
            offsets.reverse()
    if curr_tile == "|":
        offsets = [offset_north, offset_south]
    if curr_tile == "-":
        offsets = [offset_east, offset_west]
    if curr_tile == "L":
        offsets = [offset_north, offset_east]
    if curr_tile == "J":
        offsets = [offset_north, offset_west]
    if curr_tile == "7":
        offsets = [offset_south, offset_west]
    if curr_tile == "F":
        offsets = [offset_south, offset_east]

    for off in offsets:
        next_x = x+off[0]
        next_y = y+off[1]
        
        if next_x < 0 or next_y < 0 or next_x >= width or next_y >= height:
            continue
        
        next_tile = input_lines[next_y][next_x]
        if next_tile == ".":
            continue
        
        # if curr_tile == "S": # check if next tile is also connected
        if next_tile == "J" and off not in [offset_south, offset_east]:
            continue
        if next_tile == "L" and off not in [[-1, 0], [0, 1]]:
            continue
        if next_tile == "7" and off not in [[0, -1], [1, 0]]:
            continue
        if next_tile == "F" and off not in [[-1, 0], [0, -1]]:
            continue
        if next_tile == "-" and off not in [[-1, 0], [1, 0]]:
            continue
        if next_tile == "|" and off not in [[0, -1], [0, 1]]:
            continue
        
        if x+off[0] == prev_x and y+off[1] == prev_y: # dont go back
            continue
        if [x+off[0], y+off[1]] in history: # dont go even more back
            continue
        
        check(x+off[0], y+off[1], x, y, history, curr_distance)
        
    return history

history = check(start_x, start_y, None, None, [])
# visited = set([frozenset(i) for i in history])

max_distance = 0
for i in distance_table:
    for j in i:
        # print("%02d" % (j,) if j != None else "_"*2, end=" ")
        print(("X" if j > 0 else "S") if j != None else "_", end=" ")
        max_distance = max(max_distance, int(j) if j != None else 0)
    print()
max_distance = int(round(max_distance/2))

print("part 1:", max_distance)

#! part 2

area = 0
for (y, line) in enumerate(distance_table):
    within = False

    for (x, dis) in enumerate(line):
        if dis != None: # visited  before - is in the big pipe
            if input_lines[y][x] in ["|", "L", "J"]: # 7, F
                within = not within
        elif within:
            # input_lines[y][x] = "@"
            area += 1

# out = ""
# for l in input_lines:
#     out += " ".join(list(l)) + "\n"
# print(out)

print("part 2:", area)
