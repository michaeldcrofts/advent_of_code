# --- Day 1: Not Quite Lisp ---
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-1-puzzle-input.txt","r").read().splitlines()

def partOne()->int: # Return the floor Santa ends on
    global lines
    line = lines[0]
    floor = 0
    for char in line:
        if char == "(":
            floor += 1
        else:
            floor -= 1
    return floor

def partTwo()->int: # Return the index of the character that first causes floor to be negative
    global lines
    line = lines[0]
    floor = 0
    for charIdx in range(len(line)):
        if line[charIdx] == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return charIdx + 1

tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 1:", partTwo())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
