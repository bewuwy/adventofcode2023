# advent of code 2023 - day 2
# by bewu 19/12/2023

import re

input_ = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
with open("input/2.txt", "r") as f:
    input_ = f.read()

# part 1
# MAX_RED = 12
# MAX_GREEN = 13
# MAX_BLUE = 14

res = 0

for (game_i, game_log) in enumerate(input_.split("\n")):
    game_id = game_i + 1
    game_log = game_log.split(": ")[1]
    sets = game_log.split('; ')
    
    # game_ok = True # part 1
    min_blue = 0
    min_red = 0
    min_green = 0
    
    for s in sets:        
        # get blue num
        reg = re.search(r"(\d+) blue", s)
        num_blue = int(reg.group(1)) if reg else 0
        if num_blue > min_blue:
            min_blue = num_blue
        
        # get red num
        reg = re.search(r"(\d+) red", s)
        num_red = int(reg.group(1)) if reg else 0
        if num_red > min_red:
            min_red = num_red
        
        # get green num
        reg = re.search(r"(\d+) green", s)
        num_green = int(reg.group(1)) if reg else 0
        if num_green > min_green:
            min_green = num_green
        
    # print(game_id, game_ok)
        
    # if game_ok == True: # part 1
    
    power = min_blue * min_green * min_red
    res += power
    
print(res)
print(res == 2286)
