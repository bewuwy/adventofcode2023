# advent of code 2023 - day 7
# by bewu 20-21/12/2023

input_ = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
with open("input/7.txt", "r") as f:
    input_ = f.read()

hands = [i.split(" ")[0] for i in input_.splitlines()]
bids = [int(i.split(" ")[1]) for i in input_.splitlines()]

hand_to_bid = { hands[i]: bids[i] for i in range(len(hands)) }

res = 0

def part1():
    global res

    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def compare(hand_a, hand_b):
        type_a = get_hand_type(hand_a)
        type_b = get_hand_type(hand_b)
        
        if type_a > type_b:
            return 1
        if type_b > type_a:
            return -1
        
        for card_i in range(len(hand_a)):
            card_a = hand_a[card_i]
            card_b = hand_b[card_i]
        
            value_a = -cards.index(card_a)
            value_b = -cards.index(card_b)
            
            if value_a > value_b:
                return 1
            if value_b > value_a:
                return -1

    def get_hand_type(hand): # 0 - High card, 1 - One pair, 2 - two pair, 3 - three of a kind, 4 - full house, 5 - four of a kind, 6 - five of a kind
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

    n = len(hands)

    for i in range(n):
        # print(hands)
        
        already_sorted = True
        
        for j in range(n - i - 1):
            if compare(hands[j], hands[j+1]) < 0: 
                # swap values
                hands[j], hands[j+1] = hands[j+1], hands[j]
                
                already_sorted = False
                
        if already_sorted:
            break

    for (i, hand) in enumerate(hands):
        rank = n - i
        bid = hand_to_bid[hand]
        # print(rank, hand, bid)
        
        res += rank * bid

    print(res)

def part2():
    global res
    
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    def compare(hand_a, hand_b):
        type_a = get_hand_type(hand_a)
        type_b = get_hand_type(hand_b)
        
        if type_a > type_b:
            return 1
        if type_b > type_a:
            return -1
        
        for card_i in range(len(hand_a)):
            card_a = hand_a[card_i]
            card_b = hand_b[card_i]
        
            value_a = -cards.index(card_a)
            value_b = -cards.index(card_b)
            
            if value_a > value_b:
                return 1
            if value_b > value_a:
                return -1

    def get_hand_type(hand): # 0 - High card, 1 - One pair, 2 - two pair, 3 - three of a kind, 4 - full house, 5 - four of a kind, 6 - five of a kind
        hand_list = [i for i in hand]
        num_distinct = len(set(hand_list))
        
        if num_distinct == 1 or (num_distinct == 2 and "J" in hand): # five of a kind
            return 6
        elif num_distinct == 2 or (num_distinct == 3 and "J" in hand): # four of a kind / full house
            most_common_num = 0
            for c in set(hand_list):
                if c == "J":
                    continue
                num = hand_list.count(c) + hand_list.count("J")
                most_common_num = max(most_common_num, num)
            
            if most_common_num == 4:
                return 5
            else:
                return 4
        elif num_distinct == 5: # high card / one pair with joker
            if "J" in hand:
                return 1
            return 0
        else: # three o.a.k. / two pair / one pair
            most_common_num = 0
            for c in set(hand_list):
                if c == "J":
                    continue
                num = hand_list.count(c) + hand_list.count("J")
                most_common_num = max(most_common_num, num)
                
            if most_common_num == 3: # three of a kind
                return 3
            if most_common_num == 2: # one pair / two pair
                if num_distinct == 4: # one pair
                    return 1
                else:
                    return 2 # two pair

    n = len(hands)

    for i in range(n):
        # print(hands)
        
        already_sorted = True
        
        for j in range(n - i - 1):
            if compare(hands[j], hands[j+1]) < 0: 
                # swap values
                hands[j], hands[j+1] = hands[j+1], hands[j]
                
                already_sorted = False
                
        if already_sorted:
            break

    for (i, hand) in enumerate(hands):
        rank = n - i
        bid = hand_to_bid[hand]
        # print(rank, hand, bid)
        
        res += rank * bid

    print(res)
    
part2()
