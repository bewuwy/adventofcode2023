# advent of code 2023 - day 14
# by bewu 26/12/2023

import numpy as np
from functools import cache

input_ = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
with open("input/14.txt", "r") as f:
    input_ = f.read()

matrix = np.array([list(i) for i in input_.splitlines()])
height = len(matrix)
width = len(matrix[0])
# matrix_t = matrix.transpose()

def roll_north(x, y):
    global matrix
    
    curr_x = x
    curr_y = y
    
    next_y = y-1
    if next_y < 0:
        return curr_x, curr_y
    
    next_char = matrix[next_y][curr_x]
    if next_char == "#" or next_char == "O":
        return curr_x, curr_y
    
    # update matrix
    matrix[curr_y][curr_x] = "."
    matrix[next_y][curr_x] = 'O'
    
    return roll_north(curr_x, next_y)

def calculate_load(matrix):
    res = 0

    for (y, line) in enumerate(matrix):
        load_weight = height - y
        res += np.count_nonzero(line == "O") * load_weight
        
    return res

def part1():
    for (y, line) in enumerate(matrix):
        for (x, char) in enumerate(line):
            if char == "O":
                roll_north(x, y)

    # calculate load
    res = calculate_load(matrix)
        
    print("day 14 part 1:", res)

# part 2

def roll(x, y, direction, matrix):
    
    curr_x, curr_y = x, y    
    next_y, next_x = -1, -1
    
    if direction == "N":
        next_y = y - 1
        next_x = x
    elif direction == "E":
        next_y = y
        next_x = x + 1
    elif direction == "S":
        next_y = y + 1
        next_x = x
    elif direction == "W":
        next_y = y
        next_x = x - 1
    else:
        quit()
    
    if next_y < 0 or next_x < 0 or next_x >= width or next_y >= height:
        return curr_x, curr_y
    
    next_char = matrix[next_y][next_x]
    if next_char == "#" or next_char == "O":
        return curr_x, curr_y
    
    # update matrix
    matrix[curr_y][curr_x] = "."
    matrix[next_y][next_x] = 'O'
    
    return roll(next_x, next_y, direction, matrix)

@cache
def whirl_cycle(matrix_str):
    matrix = np.array([list(i) for i in matrix_str.splitlines()])
    
    # roll everything north (start at low y)
    for (y, line) in enumerate(matrix):
        for (x, char) in enumerate(line):
            if char == "O":
                roll(x, y, "N", matrix)
    
    # roll everything west (start at low x)
    matrix_t = matrix.transpose()
    
    for (x, column) in enumerate(matrix_t):
        for (y, char) in enumerate(column):
            if char == "O":
                roll(x, y, "W", matrix)

    # roll everything south (start at high y)
    for y_i in range(height):
        y = height - y_i - 1
        line = matrix[y]
        
        for (x, char) in enumerate(line):
            if char == "O":
                roll(x, y, "S", matrix)
                        
    # roll everything east (start at high x)
    matrix_t = matrix.transpose()
    
    for x_i in range(width):
        x = width - x_i - 1
        column = matrix_t[x]
        
        for (y, char) in enumerate(column):
            if char == "O":
                roll(x, y, "E", matrix)
                
    return matrix

def matrix_to_str(matrix):
    return "\n".join(["".join(i) for i in matrix])

def part2():
    global matrix
    
    states = [matrix_to_str(matrix)]
    
    while True:
        # perform cycle
        matrix = whirl_cycle(matrix_to_str(matrix))
        new_str = matrix_to_str(matrix)
        if new_str in states:
            break
        states.append(new_str)

    first_time = states.index(matrix_to_str(matrix))
    cycles = len(states) - first_time
    matrix = states[(1_000_000_000 - first_time) % cycles + first_time]
    matrix = np.array([list(i) for i in matrix.splitlines()])

    # calculate load
    res = calculate_load(matrix)

    print("day 14 part 2:", res)

part2()
