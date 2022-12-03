#--- Day 3: Rucksack Reorganization ---
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-3-puzzle-input.txt","r").read().splitlines()

def partOne()->int:     # Return sum of 'priorities' of the common characters strings split in half
    global lines
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    prioritySum = 0
    for line in lines:
        ruckOne = line[0:len(line)//2]
        ruckTwo = line[len(line)//2:]
        common = ""
        for char in ruckOne:
            if char in ruckTwo:
                common += char
        prioritySum += alphabet.find(common[0])+1
    return prioritySum

def partTwo()->int:     # Return sum of 'priorities' of the common characters from groups of 3 strings
    global lines
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    prioritySum = 0
    for lineCount in range(2,len(lines),3):     # Iterate through list of strings in steps of 3, starting at third position
        common = ""
        for char in lines[lineCount-2]:         # Iterate through each char in first of three strings
            if char in lines[lineCount-1] and char in lines[lineCount]:
                common += char
        prioritySum += alphabet.find(common[0])+1
    return prioritySum


tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 2:", partTwo())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
