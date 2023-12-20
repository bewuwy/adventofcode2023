# advent of code 2023 - day 7
# by bewu 20/12/2023

input_ = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

hands = [i.split(" ")[0] for i in input_.splitlines()]
bids = [int(i.split(" ")[1]) for i in input_.splitlines()]

sorted_hands = { i: [] for i in range(0,6+1) }

res = 0

def get_hand_type(hand): # 0 - High card, 1 - One pair, 2 - two pair, 3 - three of a kind, 4 - full house, 5 - four of a kind, 6- five of a kind
    hand_list = [i for i in hand]
    num_distinct = len(set(hand_list))
    
    if num_distinct == 1: # five of a kind
        return 6
    elif num_distinct == 2: # four of a kind / full house
        num_first = hand_list.count(hand_list[0])
        if num_first == 4 or num_first == 1:
            return 5
        else:
            return 4
    elif num_distinct == 5: # high card
        return 0
    else: # three o.a.k. / two pair / one pair
        most_common_num = 0
        for c in set(hand_list):
            most_common_num = max(most_common_num, hand_list.count(c))
            
        if most_common_num == 3: # three of a kind
            return 3
        if most_common_num == 2: # one pair / two pair
            if num_distinct == 4: # one pair
                return 1
            else:
                return 2 # two pair

for (i, hand) in enumerate(hands):
    
    t = get_hand_type(hand)
    sorted_hands[t].append((hand, bids[i]))
    
print(sorted_hands)
    
rank = 1

for t in sorted_hands:
    
    pass
    
print(0)
