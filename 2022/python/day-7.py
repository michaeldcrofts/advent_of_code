#--- Day 7: No Space Left On Device ---
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-7-puzzle-input.txt","r").read().splitlines()

def createFileStructure()->dict: # Process terminal output into dictionary file structure
    global lines
    fs = {"/":{}}     # Key value pairs will either be foldername: dict, or filename: int
    level = []     # Keeps track of the current depth level we are operating in, changed by the cd command
    for line in lines:
        if line[0] == "$":  # Process command
            if line == "$ cd ..":    # Change to level above current
                if len(level) > 1:
                    level = level[0:-1]
            elif line[0:5] == "$ cd ":  # Enter new directory
                level.append(line[5:])
        elif line[0:3] == "dir": # Create new directory
            handle = fs     # memory address
            for key in level:
                handle = handle[key]    # memory address of sub-level dictionary
            handle[line[4:]]={}
        elif line[0].isnumeric():   # Create new file
            handle = fs     # memory address
            for key in level:
                handle = handle[key]    # memory address of sub-level dictionary
            handle[line.split(" ")[1]] = int(line.split(" ")[0])
    return fs

def directorySize(fs: dict, dirSizeArr: dict=[])->int:   # Return the size of a directory and all subdirectories
    size = 0
    for key in fs:
        if type(fs[key]) == dict: # Sub directory, recursively call this subroutine
            size += directorySize(fs[key], dirSizeArr)
        else:
            size += fs[key]
    dirSizeArr.append(size)
    return size

def showFileStructure(fs: dict, level:int=0):    # Friendly print of the file structure, level used to get correct level of indentation
    for key in fs:
        if type(fs[key]) == dict:   # Sub folder, print folder name and then recursively call this subroutine
            print("  "*level, end="")  # Print indentation
            print("-", key, "(dir) size="+str(directorySize(fs[key])))
            showFileStructure(fs[key], level + 1)
        else:   # Leaf file
            print("  "*level, end="")  # Print indentation
            print("-", key, "(file, size="+str(fs[key]) + ")")

def partOne():
    fs = createFileStructure()
    #showFileStructure(fs)
    dirSizes = []
    total = directorySize(fs,dirSizes)
    sum = 0 
    for f in dirSizes:
        if f <= 100000:
            sum += f
    return sum

def partTwo():
    fs = createFileStructure()
    dirSizes = []
    total = directorySize(fs,dirSizes)
    available = 70000000 - total
    target = 30000000 - available
    candidates = []
    for f in dirSizes:
        if f >= target:
            candidates.append(f)
    candidates = sorted(candidates)
    return candidates[0]

tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 2:", partTwo())


print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()