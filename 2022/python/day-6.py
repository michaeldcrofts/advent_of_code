#--- Day 6: Tuning Trouble ---
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-6-puzzle-input.txt","r").read().splitlines()

def findUniqueStr(source:str,numberOfChars:int)->int: # Return the character index of the first unique character string of size n within source
    for charCount in range(numberOfChars,len(source)+1):
        header = source[charCount-numberOfChars:charCount]
        unique = True
        for char in header:
            if header.count(char) > 1:
                unique = False
        if unique:
           return charCount

def partOne()->int:     # Return the character index of the first 4-character unique string
    global lines
    line = lines[0]
    return findUniqueStr(line,4)

def partTwo():          # Return the character index of the first 14-character unique string
    global lines
    line = lines[0]
    return findUniqueStr(line,14)

tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 2:", partTwo())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
