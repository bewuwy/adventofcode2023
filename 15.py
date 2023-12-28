# advent of code 2023 - day 15
# by bewu 28/12/2023

input_ = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
with open("input/15.txt", "r") as f:
    input_ = f.read()

steps = input_.split(",")

def hash_(s):
    res = 0
    
    for char in s:
        res += ord(char)
        res *= 17
        res = res % 256
        
    return res
        
def part1():
    res = 0
    for s in steps:
        res += hash_(s)

    print(res)

def part2():
    boxes = [[] for _ in range(256)] # boxes: [ box: [ lens: [label, strength], ... ], ... ]
    
    for s in steps:
        box_n = hash_(s.split("=")[0].split("-")[0]) # hash of lens label
        curr_lenses = boxes[box_n]
        
        if "=" in s:
            focal_strength = s[-1]
            label = s.split("=")[0]

            # with same label
            curr_labels = [i[0] for i in curr_lenses]
            try:
                l_index = curr_labels.index(label)
                curr_lenses[l_index] = [label, focal_strength]
            except ValueError: # add a new lens
                curr_lenses.append([label, focal_strength])
            
        elif "-" in s:
            label = s.split("-")[0]
            curr_labels = [i[0] for i in curr_lenses]
            
            try:
                l_index = curr_labels.index(label)            
                curr_lenses.pop(l_index)
            except ValueError:
                pass

    # # print boxes
    # for b_n in range(len(boxes)):
    #     if len(boxes[b_n]) > 0:
    #         print("box", b_n, boxes[b_n])
            
    # calculate focusing power
    res = 0
    
    for (b_n, b) in enumerate(boxes):
        if len(b) == 0:
            continue
        
        for (l_n, lens) in enumerate(b):
            power = 1 + b_n # 1 plus box number
            power *= 1 + l_n # slot number of the lens within the box
            power *= int(lens[1]) # focal length of the lens
            
            res += power

    print(res)

part2()
