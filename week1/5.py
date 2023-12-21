# advent of code 2023 - day 5
# by bewu 20/12/2023

input_ = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
with open("input/5.txt", "r") as f:
    input_ = f.read()
input_list = input_.split("\n\n")

# get seeds
seeds_text = input_list[0].split(": ")[1]
seeds = [int(i) for i in seeds_text.split(" ")]
seeds_starts = seeds[::2]
seeds_lengths = seeds[1::2]

seeds_ranges = []
for i in range(len(seeds_starts)):
    seeds_ranges.append([seeds_starts[i], seeds_lengths[i]])
    
print(seeds_ranges)

for map_i in range(1, len(input_list)):
    print("map", map_i)
    
    map_text = input_list[map_i]
    print(map_text, end="\n\n")
    
    map_lines = map_text.splitlines()[1:]
    
    for seed_i in range(len(seeds_ranges)):
        
        seed_start, seed_length = seeds_ranges[seed_i]
        
        can_skip = True
        best_start = 99999999999999
        
        for (m_i, m_line) in enumerate(map_lines):
            (dest_start, source_start, length) = [int(i) for i in m_line.split(" ")]
            
            seed_max = seed_start + seed_length
            if seed_max < source_start or seed_start > (source_start+length):
                # can_skip = True if can_skip != False else False
                print("no solutions")
                continue
            
            if seed_start < source_start:
                print("some solutions")
                # can_skip = True
            else:
                print("inf solutions")
                can_skip = False
            
            out_change = dest_start - source_start
            best_start = min(best_start, max(source_start, seed_start) + out_change)
            
            # print(seed_i, m_i, can_skip)
            
        print("can skip:", can_skip)
        if can_skip:
            best_start = min(seed_start, best_start)
            
        print("seed", seed_i, best_start)
        seeds_ranges[seed_i][0] = best_start
        
seeds_starts = [i[0] for i in seeds_ranges]

lowest = min(seeds_starts)
print(f"\n{lowest}")
