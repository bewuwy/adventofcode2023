# advent of code 2023 - day 12
# by bewu 23/12/2023

input_ = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
input_lines = input_.splitlines()

res = 0
for line in input_lines:
    print(line)
    l = list(line)

    question_n = l.count("?")
    options = 2**question_n
    
    for i in range(options):
        l_ = l.copy()
        
        bin_option = bin(i)[2:]
        bin_option = "0" * (question_n - len(bin_option)) + bin_option
        
        print(bin_option)
        
        q_i = 0
        for (ch_i, char) in enumerate(l_):
            if char != "?":
                continue
            
            if bin_option[q_i] == "1": # working
                l_[ch_i] = "."
            else:
                l_[ch_i] = "#"
                
            q_i += 1
            
        print("".join(l_))

    quit()
