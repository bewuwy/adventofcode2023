# advent of code 2023 - day 6
# by bewu 20/12/2023

input_ = """Time:      7  15   30
Distance:  9  40  200"""
with open("input/6.txt", "r") as f:
    input_ = f.read()

# times = [int(i) for i in input_.splitlines()[0].split(": ")[1].strip().split("  ")]
# record_distances = [int(i) for i in input_.splitlines()[1].split(": ")[1].strip().split("  ")]
time = int(input_.splitlines()[0].split(": ")[1].replace(" ", ""))
record_distance = int(input_.splitlines()[1].split(": ")[1].replace(" ", ""))

acceleration = 1

print(time)
print(record_distance)

res = 0 # 1

# for race_n in range(len(times)):
speed = 0
# options = 0

for time_loading in range(1, time):
    speed = time_loading * acceleration
    distance = (time - time_loading) * speed
    
    if distance > record_distance:
        # options += 1
        res += 1
        
# res *= options
    
print(res)
