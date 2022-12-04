#--- Day 2: I Was Told There Would Be No Math ---
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-2-puzzle-input.txt","r").read().splitlines()

def rectArea(length:int,width:int,height:int)->int: # Return the area of a cuboid
    return 2*length*width + 2*width*height + 2*height*length

def partOne()->int:     # Return the amount of paper needed to wrap each cuboid
    global lines
    totalPaper = 0
    for line in lines:
        dimensions = list(map(lambda x:int(x), line.split("x")))
        length = dimensions[0]
        width = dimensions[1]
        height = dimensions[2]
        totalPaper += rectArea(length,width,height) + sorted([length*width,width*height,height*length])[0]
    return totalPaper

def partTwo()->int:     # Return the amount of ribbon needed
    global lines
    totalRibbon = 0
    for line in lines:
        dimensions = list(map(lambda x:int(x), line.split("x")))
        length = dimensions[0]
        width = dimensions[1]
        height = dimensions[2]
        ribbon = sorted([length*2+width*2,width*2+height*2,height*2+length*2])[0]   # Smallest perimeter
        bow = length*width*height
        totalRibbon += ribbon+bow
    return totalRibbon


tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 2:", partTwo())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
