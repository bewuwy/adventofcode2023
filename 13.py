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

res = 0

for pattern in input_.split("\n\n"):
    print(pattern)
    
    p = pattern.splitlines()
    matrix = np.array([list(i) for i in p])
    matrix__ = matrix.transpose()
    width = len(p[0])

    finished = False
    
    # vertical reflection
    for refl in range(width):        
        
        works = False
        for dis_from_reflection in range(1, width // 2):
            if refl - dis_from_reflection < 0 or refl + dis_from_reflection >= width:
                break
            
            # print('dis', dis_from_reflection)
            
            col_left = matrix__[refl - (dis_from_reflection - 1)]
            col_right = matrix__[refl + dis_from_reflection]
            
            # print(col_left)
            # print(col_right)
            
            if np.array_equal(col_left, col_right):
                works = True
            else:
                works = False
                                            
        if works:
            print("vertical WORKS", refl)
            res += refl+1
            finished = True
            break
        
    if finished:
        continue
    
    # horizontal reflection
            
    quit()
