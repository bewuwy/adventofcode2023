# advent of code 2023 - day 12
# by bewu 23,26/12/2023
#######################################################################################
# used: https://github.com/savbell/advent-of-code-one-liners/blob/master/2023/day-12.py

from functools import cache

input_ = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
with open("input/12.txt", "r") as f:
    input_ = f.read()

input_lines = input_.splitlines()

def part1():
    res = 0
    for line in input_lines:
        # print(line)
        l = list(line)
        correct_numbers = [int(i) for i in line.split(" ")[1].split(',')]

        question_n = l.count("?")
        options = 2**question_n
        
        for i in range(options):
            l_ = l.copy()
            
            bin_option = bin(i)[2:]
            bin_option = "0" * (question_n - len(bin_option)) + bin_option

            q_i = 0
            for (ch_i, char) in enumerate(l_):
                if char != "?":
                    continue
                
                if bin_option[q_i] == "1": # working
                    l_[ch_i] = "."
                else:
                    l_[ch_i] = "#"
                    
                q_i += 1
                
            o = "".join(l_).split(" ")[0]
            # print(o)
            
            o_numbers = []
            curr_num = 0
            for char in o:
                if char == "#":
                    curr_num += 1
                else:
                    if curr_num > 0:
                        o_numbers.append(curr_num)
                    curr_num = 0
            if curr_num > 0:
                o_numbers.append(curr_num)
                    
            # print(o_numbers)
            if o_numbers == correct_numbers:
                res += 1

    print("day 12 part 1:", res)

@cache
def count(springs_str, correct_numbers, group_loc=0):
    if not springs_str:
        return not correct_numbers and not group_loc
    
    res = 0
    possibilities = ['.', '#'] if springs_str[0] == '?' else springs_str[0]
    for p in possibilities:
        if p == '#':
            res += count(springs_str[1:], correct_numbers, group_loc + 1)
        else:
            if group_loc > 0:
                if correct_numbers and correct_numbers[0] == group_loc:
                    res += count(springs_str[1:], correct_numbers[1:])
            else:
                res += count(springs_str[1:], correct_numbers)
    return res


def part2():
    res = 0
    for line in input_lines:
        # print(line)
        correct_numbers = [int(i) for i in line.split(" ")[1].split(',')] * 5
        springs = "?".join([line.split(" ")[0]] * 5) + '.'
        # print(springs)
        # print(correct_numbers)
        
        c = count("".join(springs), tuple(correct_numbers))
        # print(c)
        
        res += c
    
    print("day 12 part 2:", res)

part2()
