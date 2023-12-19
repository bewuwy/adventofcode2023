# advent of code 2023 - day 3
# by bewu 19/12/2023

input_ = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
with open("input/3.txt", "r") as f:
    input_ = f.read()

input_table = input_.splitlines()

INPUT_WIDTH = len(input_table[0])
INPUT_HEIGHT = len(input_table)

res = 0

parts_table = [
    [None for _ in range(INPUT_WIDTH)] for _ in range(INPUT_HEIGHT)
]

# part_numbers = [] # list of (start_point:(line, symbol_i), num: int)

def is_part(symbol_i: int, line_i: int) -> bool:
    if symbol_i < 0 or line_i < 0 or symbol_i >= INPUT_WIDTH or line_i >= INPUT_HEIGHT:
        return False
    
    symbol = input_table[line_i][symbol_i]
    
    return symbol != "." and not symbol.isdigit()

def check_spot(symbol_i, line_i, curr_num="", num_valid=False):
    global res
    global part_numbers
    
    # if checked_table[line_i][symbol_i] == True:
    #     return 0
    # checked_table[line_i][symbol_i] = True
    
    # if there is a number to the left and just started, skip
    if symbol_i > 0 and input_table[line_i][symbol_i-1].isnumeric() and curr_num == "":
        return 0
    
    if symbol_i == INPUT_WIDTH or line_i == INPUT_HEIGHT:
        return None
    
    s = input_table[line_i][symbol_i]
    if not s.isnumeric():
        return None
    
    if num_valid == False: # check if number valid - is there any symbol neighbouring it?
        
        for line_offset in [-1, 0, 1]:
            for symbol_offset in [-1, 0, 1]:
                if line_offset == 0 and symbol_offset == 0:
                    continue
        
                valid = is_part(symbol_i+symbol_offset, line_i+line_offset)
                if valid == True:
                    num_valid = True
                    break
    
    # check the next symbol
    num = curr_num + s
    next_num = check_spot(symbol_i+1, line_i, curr_num=num, num_valid=num_valid)
    
    # if isinstance(next_num, list):
    #     print("LIST")
    #     return next_num
    
    if next_num:
        num += next_num
    else:
        # print("end of num", num)
        # print("ended at", symbol_i, line_i)
        # print("started at", symbol_i - len(num) + 1, line_i)
    
        # print("valid", num_valid)
        if num_valid:
            # res += int(num)
            # part_numbers.append(((symbol_i + 1 - len(num), line_i), num))
            
            for x in range(symbol_i - len(num) + 1, symbol_i+1):
                parts_table[line_i][x] = num
            
            # return [int(num)]
    
    return num

for (l_i, l) in enumerate(input_.splitlines()):
    # print(l)
    for (s_i, s) in enumerate(l):
        r = check_spot(s_i, l_i)
    
for (l_i, l) in enumerate(input_.splitlines()):
    print(l)
    for (s_i, s) in enumerate(l):
        if s != "*": # not GEAR
            continue
        
        parts_adjacent = set([None])
        
        for line_offset in [-1, 0, 1]:
            for symbol_offset in [-1, 0, 1]:
                if line_offset == 0 and symbol_offset == 0:
                    continue
                
                parts_adjacent.add(parts_table[l_i+line_offset][s_i+symbol_offset])

        if len(parts_adjacent) != 3: # not adjacent to 2 parts
            continue

        parts_adjacent.remove(None)
        parts_adjacent = list(parts_adjacent)
        
        res += int(parts_adjacent[0]) * int(parts_adjacent[1])

# for y in parts_table:
#     print(y)

print(res)
# print(res == 4361)
