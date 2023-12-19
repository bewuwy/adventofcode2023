# advent of code 2023 - day 1
# by bewu 19/12/2023

input_ = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
with open("input/1.txt", "r") as f:
    input_ = f.read()
    
NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

res = 0
for (line_i, line) in enumerate(input_.split("\n")):
    # print(line)
    
    first = None
    last = None
    
    for (symbol_i, symbol) in enumerate(line):
        if symbol.isnumeric():
            if first == None:
                first = symbol
                
            last = symbol
        else:
            for (n_i, n_spelled) in enumerate(NUMBERS):
                if symbol_i + len(n_spelled) <= len(line): # there is enough room for the number
                    num_ok = True
                    for (j, n_letter) in enumerate(n_spelled):
                        if line[symbol_i + j] != n_letter: 
                            num_ok = False
                            break
                    if num_ok:
                        if first == None:
                            first = str(n_i + 1)
                        last = str(n_i + 1)
                        
                        break
                        
    # print(first, last)
    num = int(first+last)
    res += num
    
print(res)
# print(res == 281)
