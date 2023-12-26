# advent of code 2023 - day 9
# by bewu 21/12/2023

input_ = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
with open("input/9.txt", "r") as f:
    input_ = f.read()

variables_history = [[int(j) for j in i.split(" ")] for i in input_.splitlines()]
derivatives = [[] for _ in range(len(variables_history))]

def part1():
    res = 0

    for (v_i, v) in enumerate(variables_history):
        # print(v)

        curr_derivative = []
        for i in range(len(v)-1):
            change = v[i+1] - v[i]
            curr_derivative.append(change)
            
        derivatives[v_i].append(curr_derivative)

        while sum(curr_derivative) != 0:
            new_derivative = []
            
            for i in range(len(curr_derivative)-1):
                change = curr_derivative[i+1] - curr_derivative[i]
                new_derivative.append(change)
                
            curr_derivative = new_derivative
            derivatives[v_i].append(curr_derivative)

        
        # find next value
        derivatives[v_i].insert(0, v)
        
        next_value = 0
        for i in range(len(derivatives[v_i])):
            next_value += derivatives[v_i][-(i+1)][-1]
        
        # print(next_value)
        res += next_value
        
    print(res)

def part2():
    res = 0

    for (v_i, v) in enumerate(variables_history):
        print(v)

        curr_derivative = []
        for i in range(len(v)-1):
            change = v[i+1] - v[i]
            curr_derivative.append(change)
            
        derivatives[v_i].append(curr_derivative)

        while sum(curr_derivative) != 0:
            new_derivative = []
            
            for i in range(len(curr_derivative)-1):
                change = curr_derivative[i+1] - curr_derivative[i]
                new_derivative.append(change)
                
            curr_derivative = new_derivative
            derivatives[v_i].append(curr_derivative)

        # print(derivatives[v_i])
        
        # find next value
        derivatives[v_i].insert(0, v)
        
        prev_value = 0
        for i in range(len(derivatives[v_i])):
            # print(prev_value)
            prev_value += (-1)**(i) * derivatives[v_i][i][0]
        
        print(prev_value)
        res += prev_value
        
        # quit()
        
    print(res)

part2()
