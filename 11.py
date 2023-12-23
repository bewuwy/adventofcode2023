# advent of code 2023 - day 11
# by bewu 23/12/2023

input_ = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
with open("input/11.txt", "r") as f:
    input_ = f.read()

def part1():
    input_list = input_.splitlines()
    width = len(input_list[0])
    height = len(input_list)
    new_input_list = input_.splitlines()

    # expand the universe

    # rows
    num_rows_added = 0
    for (i, row) in enumerate(input_list):
        if "#" not in row: # empty row
            new_input_list.insert(i+1+num_rows_added, "."*width)
            num_rows_added += 1

    input_list = [list(i) for i in new_input_list.copy()]
    new_input_list = [list(i) for i in new_input_list]
    width = len(input_list[0])
    height = len(input_list)

    # columns
    num_col_added = 0
    for c_i in range(width):
        empty = True
        for r_i in range(height):
            if input_list[r_i][c_i] == "#":
                empty = False
                break
        
        if empty:
            for r_i in range(height):
                new_input_list[r_i].insert(c_i+1+num_col_added, ".")
            num_col_added += 1

    input_list = [i.copy() for i in new_input_list]
    width = len(input_list[0])
    height = len(input_list)

    # for i in input_list:
    #     for j in i:
    #         print(j, end="")
    #     print()

    # locate galaxies
    galaxies = []
    for (y, line) in enumerate(input_list):
        for (x, char) in enumerate(line):
            if char == "#":
                # print(i, j)
                galaxies.append((x, y))

    # go through each pair

    shortest_path = {}
    for galaxy_a in galaxies:
        for galaxy_b in galaxies:
            if (galaxy_b, galaxy_a) in shortest_path or galaxy_a == galaxy_b:
                continue
            
            dy = galaxy_a[1] - galaxy_b[1]
            dx = galaxy_a[0] - galaxy_b[0]

            d = abs(dy) + abs(dx) #math.sqrt(dy**2 + dx**2)
            shortest_path[(galaxy_a, galaxy_b)] = d

    print("day 11 part 1:", sum(shortest_path.values()))

def part2():
    input_list = input_.splitlines()
    width = len(input_list[0])
    height = len(input_list)
    new_input_list = input_.splitlines()

    # expand the universe

    # rows
    num_rows_added = 0
    for (i, row) in enumerate(input_list):
        if "#" not in row: # empty row
            new_input_list.insert(i+1+num_rows_added, "X"*width)
            num_rows_added += 1

    input_list = [list(i) for i in new_input_list.copy()]
    new_input_list = [list(i) for i in new_input_list]
    width = len(input_list[0])
    height = len(input_list)

    # columns
    num_col_added = 0
    for c_i in range(width):
        empty = True
        for r_i in range(height):
            if input_list[r_i][c_i] == "#":
                empty = False
                break
        
        if empty:
            for r_i in range(height):
                new_input_list[r_i].insert(c_i+1+num_col_added, "X")
            num_col_added += 1

    input_list = [i.copy() for i in new_input_list]
    width = len(input_list[0])
    height = len(input_list)

    for i in input_list:
        for j in i:
            print(j, end="")
        print()

    # locate galaxies
    galaxies = []
    for (x, line) in enumerate(input_list):
        for (y, char) in enumerate(line):
            if char == "#":
                # print(i, j)
                galaxies.append((x, y))

    # go through each pair
    expansion_multiplier = 10**6
    
    # update galaxies coordinates
    for (g_i, g) in enumerate(galaxies):
        print(g)
        
        # update y
        new_y = g[1]
        for y in range(g[1]):
            if input_list[g[0]][y] == "X":
                new_y += expansion_multiplier - 2
        
        # update x
        new_x = g[0]
        for x in range(g[0]):
            if input_list[x][g[1]] == "X":
                new_x += expansion_multiplier - 2
                
        galaxies[g_i] = (new_x, new_y)
        print(galaxies[g_i])
    
    def combinations(elements):
        return [(a, b) for idx, a in enumerate(elements) for b in elements[idx + 1:]]

    shortest_path = {}
    for (galaxy_a, galaxy_b) in combinations(galaxies):            
        dy = galaxy_a[1] - galaxy_b[1]
        dx = galaxy_a[0] - galaxy_b[0]

        # x_range = range(min(galaxy_a[0], galaxy_b[0]), max(galaxy_a[0], galaxy_b[0]))
        # y_range = range(min(galaxy_a[1], galaxy_b[1]), max(galaxy_a[1], galaxy_b[1]))

        # # calculate dy and dx
        # dy = 0
        # for y in y_range:
        #     char = input_list[y][min(galaxy_a[0], galaxy_b[0])]
        #     if char == "X":
        #         dy += expansion_multiplier
        #     else:
        #         dy += 1
                
        # dx = 0
        # for x in x_range:
        #     char = input_list[min(galaxy_a[1], galaxy_b[1])][x]
        #     if char == "X":
        #         dx += expansion_multiplier
        #     else:
        #         dx += 1

        d = abs(dy) + abs(dx)
        shortest_path[(galaxy_a, galaxy_b)] = d

    print("day 11 part 2:", sum(shortest_path.values()))

part2()
