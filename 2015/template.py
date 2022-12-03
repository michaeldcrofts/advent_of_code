#
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-1-puzzle-input.txt","r").read().splitlines()

def partOne():
    global lines

def partTwo():
    global lines

tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 1:", partTwo())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
