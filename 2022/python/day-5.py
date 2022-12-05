#--- Day 5: Supply Stacks ---
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-5-puzzle-input.txt","r").read().splitlines()

def makeStacks(data:list, colWidth:int, colSep:str=",") -> list:    # Take a list of strings, organised into columns and return 2-d array
    fullData = []
    noOfStacks = len(data[0])//(colWidth+len(colSep))+1
    for count in range(noOfStacks):
        fullData.append([])
    for line in data:
        for count in range(noOfStacks):
            item = line[(count*(colWidth+len(colSep))):(count*(colWidth+len(colSep)))+(colWidth+len(colSep))]
            item = item.replace(colSep, "")
            if len(item):
                fullData[count].append(item)
    for stack in fullData:
        stack.reverse()      
    return fullData

def partOne()->str:     # Process stack moves and return the top item from each stack as a string
    global lines
    count = 0
    while lines[count] != "": # find end of stack data
        count += 1
    stacks = makeStacks(lines[0:count-1], 3, " ")
    count += 1
    while count < len(lines):
        move = lines[count].split(' ')
        source = int(move[3])-1
        dest = int(move[5])-1
        amount = int(move[1])
        for counter in range(amount):
            stacks[dest].append(stacks[source].pop())
        count += 1
    outputString = ""
    for stack in stacks:
        if len(stack):
            outputString += stack[-1]
    return outputString.replace("[", "").replace("]", "")

def partTwo()->str:     # Process stack moves, with multiple at a time, and return the top item from each stack as a string
    global lines
    count = 0
    while lines[count] != "": # find end of stack data
        count += 1
    stacks = makeStacks(lines[0:count-1], 3, " ")
    count += 1
    while count < len(lines):
        move = lines[count].split(' ')
        source = int(move[3])-1
        dest = int(move[5])-1
        amount = int(move[1])
        temp = []
        for counter in range(amount):
            temp.append(stacks[source].pop())
        temp.reverse()
        for item in temp:
            stacks[dest].append(item)
        count += 1
    outputString = ""
    for stack in stacks:
        if len(stack):
            outputString += stack[-1]
    return outputString.replace("[", "").replace("]", "")

tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 2:", partTwo())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
