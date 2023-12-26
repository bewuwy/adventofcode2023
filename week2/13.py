# advent of code 2023 - day 13
# by bewu 26/12/2023

import numpy as np

input_ = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
# input_ = """.###.####
# .##.##..#
# .###.####
# #....#..#
# ....#....
# ##.##....
# ##.###..#
# #..#..##.
# .#...#..#
# ....#....
# ##.######
# ...###.##
# #.###....
# ##.#.####
# ##.#.####"""
with open("input/13.txt", "r") as f:
    input_ = f.read()

def find_reflection(pattern, matrix, ignore_result=None):
    matrix__ = matrix.transpose()
    width = len(pattern[0])
    height = len(pattern)

    # vertical reflection
    for refl in range(width):        
        
        works = False
        for dis_from_reflection in range(0, width // 2 + 1):
            if refl - dis_from_reflection < 0 or refl + dis_from_reflection + 1 >= width:
                break
    
            col_left = matrix__[refl - (dis_from_reflection)]
            col_right = matrix__[refl + (dis_from_reflection + 1)]
            
            if np.array_equal(col_left, col_right):
                # print('dis', dis_from_reflection)
                # print(refl - (dis_from_reflection), col_left)
                # print(refl + (dis_from_reflection + 1), col_right)
                
                works = True
            else:
                works = False
                break
                                            
        if works and (not ignore_result or refl+1 != ignore_result):
            print("vertical WORKS", refl)
            return refl+1
    
    # horizontal reflection
    for refl in range(height):        
        
        works = False
        for dis_from_reflection in range(0, height // 2 + 1):
            if refl - dis_from_reflection < 0 or refl + dis_from_reflection + 1 >= height:
                break
                        
            col_up = matrix[refl - (dis_from_reflection)]
            col_down = matrix[refl + (dis_from_reflection + 1)]
            
            # print(col_left)
            # print(col_right)
            
            if np.array_equal(col_up, col_down):
                works = True
            else:
                works = False
                break

        if works and (not ignore_result or (refl+1) * 100 != ignore_result):
            print("horizontal WORKS", refl)
            return (refl+1) * 100

def part1():
    res = 0

    for pattern in input_.split("\n\n"):
        print()
        print(pattern)
        
        p = pattern.splitlines()
        matrix = np.array([list(i) for i in p])

        res += find_reflection(p, matrix)

    print(res)

def part2():
    res = 0

    for pattern in input_.split("\n\n"):
        print()
        
        p = pattern.splitlines()
        matrix = np.array([list(i) for i in p])
        width = len(p[0])
        height = len(p)
                
        og_result = find_reflection(p, matrix)

        finished = False
        
        for changed_x in range(width):
            for changed_y in range(height):
                
                matrix_ = matrix.copy()
                
                # update smudge
                matrix_[changed_y][changed_x] = "#" if matrix_[changed_y][changed_x] == "." else "."
        
                new_result = find_reflection(p, matrix_, og_result)
                
                if not new_result:
                    continue
                
                if new_result != og_result:
                    res += new_result
                    finished = True
                    break
                
            if finished == True:
                break

        if finished: 
            continue
            
    print(res)

part2()
