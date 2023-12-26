# advent of code 2023 - day 8
# by bewu 21/12/2023

from math import lcm as math_lcm

# input_ = """LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""
input_ = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""
with open("input/8.txt", "r") as f:
    input_ = f.read()

instructions = list(input_.splitlines()[0])
places = input_.splitlines()[2:]
place_to_available = {}

for i in range(len(places)):
    place_name = places[i].split(" = ")[0]
    places_available = places[i].split(" = ")[1].removeprefix("(").removesuffix(")").split(", ")
    
    places[i] = [place_name, places_available]
    place_to_available[place_name] = places_available

def part1():
    current_place = "AAA"
    dest_place = "ZZZ"
    
    steps = 0

    while current_place != dest_place:
        current_instruction = instructions[steps % len(instructions)]
        
        if current_instruction == "L":
            current_place = place_to_available[current_place][0]
        else:
            current_place = place_to_available[current_place][1]
        
        steps += 1

    print(steps)
    
def part2():
    
    # get start places
    current_places = []
    for p in places:
        if p[0][-1] == "A":
            current_places.append(p[0])
        
    steps = 0
    minimum_steps = [None for _ in range(len(current_places))]

    while minimum_steps.count(None) > 0:
        
        current_instruction = instructions[steps % len(instructions)]
        
        # print(steps)
        # print(minimum_steps)
            
        for place_i in range(len(current_places)):
            
            # print(place_i, current_places[place_i])
            
            if minimum_steps[place_i] != None:
                continue
            
            if current_instruction == "L":
                current_places[place_i] = place_to_available[current_places[place_i]][0]
            else:
                current_places[place_i] = place_to_available[current_places[place_i]][1]
            
            # print(current_places[place_i])
            
            if current_places[place_i][-1] == "Z":
                minimum_steps[place_i] = steps + 1
            
        steps += 1

    print(minimum_steps)
    print(math_lcm(*minimum_steps))

part2()
