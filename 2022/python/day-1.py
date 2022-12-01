# --- Day 1: Calorie Counting ---
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-1-puzzle-input.txt","r").read().splitlines()

def partOne() ->int:    # Return the highest number of calories carried by an elf
    global lines
    elves = []
    calories = 0
    for line in lines:
        if line == '': 
            elves.append(calories)
            calories = 0
        else:
            calories += int(line)
    elves.append(calories)
    elves = sorted(elves, reverse=True)
    return elves[0]

def partTwo() -> int:    # Return the sum of the highest three lots of calories carried by an elves
    global lines
    elves = []
    calories = 0
    for line in lines:
        if line == '':
            elves.append(calories)
            calories = 0
        else:
            calories += int(line)
    elves.append(calories)
    elves = sorted(elves, reverse=True)
    return elves[0] + elves[1] + elves[2]

tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 2:", partTwo())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
