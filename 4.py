# advent of code 2023 - day 4
# by bewu 20/12/2023

input_ = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
with open("input/4.txt", "r") as f:
    input_ = f.read()
input_list = input_.splitlines()

res = 0

def process_card(card_num):
    global res
    
    text = input_list[card_num]
    
    (winning, my) = text.split(" | ")
    
    winning = set([int(i) if i.isnumeric() else None for i in winning.split(" ")])
    my = set([int(i) if i.isnumeric() else None for i in my.split(" ")])
    
    winning.discard(None)
    my.discard(None)

    num_won = len(my.intersection(winning))
    res += num_won
    
    # print(f"won {num_won} cards")
    
    for c in range(card_num+1, card_num+num_won+1):
        # print(f"won copy of {c}")
        process_card(c)

for l in range(len(input_list)):
    # print(f"original {l}")
    
    print(l)
    
    process_card(l)
    
res += len(input_list)
    
print(res)
