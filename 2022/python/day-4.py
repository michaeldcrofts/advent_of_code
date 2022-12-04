#--- Day 4: Camp Cleanup ---
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-4-puzzle-input.txt","r").read().splitlines()

def isWithin(a,b)->bool:    # Given two iterables it returns true if a is entirely encompassed by b
    if len(a) > len(b):
        return False
    count = 0
    for item in a:
        if item in b:
            count += 1
    if count == len(a):
        return True
    return False

def overlap(a,b)->bool:     # Given two iterables it returns true if any of a is present in b
    for item in a:
        if item in b:
            return True
    return False

def partOne()->int:         # Returns the number of times an elf's assignment (from a pair) is entirely encapsulated by the other in the pair
    global lines
    contains = 0
    for line in lines:
        assignment = line.split(",")
        first = assignment[0]
        second = assignment[1]
        elf1 = []
        elf2 = []
        for i in range(int(first.split("-")[0]),int(first.split("-")[1])+1):
            elf1.append(i)
        for i in range(int(second.split("-")[0]),int(second.split("-")[1])+1):
            elf2.append(i)
        if isWithin(elf1,elf2) or isWithin(elf2,elf1):
            contains += 1
    return contains

def partTwo()->int:         # Returns the number of assignments which overlap
    global lines
    contains = 0
    for line in lines:
        assignment = line.split(",")
        first = assignment[0]
        second = assignment[1]
        elf1 = []
        elf2 = []
        for i in range(int(first.split("-")[0]),int(first.split("-")[1])+1):
            elf1.append(i)
        for i in range(int(second.split("-")[0]),int(second.split("-")[1])+1):
            elf2.append(i)
        if overlap(elf1,elf2) or overlap(elf2,elf1):
            contains += 1
    return contains

tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 2:", partTwo())


print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()