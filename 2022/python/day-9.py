#--- Day 9: Rope Bridge ---
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-9-puzzle-input.txt","r").read().splitlines()

def createGrid(rows:int, cols:int, initChar:chr = ".") -> list:   # Return a 2-d array of x,y size.
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(initChar)
        grid.append(row)
    return grid

def showGrid(grid: list):   # Output a visualisation of the 2-d array, useful for debugging!
    for row in grid:
        for x in row:
            print(x,sep="",end="")
        print()
    print()

def findGridSize()->list:   # Return a 2-d array
    global lines
    x = y = 0
    largestX = largestY = smallestX = smallestY = 0
    for line in lines:
        direction = line.split(" ")[0]
        amount = int(line.split(" ")[1])
        if direction == "R":
            x += amount
        elif direction == "L":
            x -= amount
        elif direction == "U":
            y += amount
        elif direction == "D":
            y -= amount
        if x > largestX:
            largestX = x
        elif x < smallestX:
            smallestX = x
        if y > largestY:
            largestY = y
        elif y < smallestY:
            smallestY = y
    print("X:", smallestX, "to", largestX)
    print("Y:", smallestY, "to", largestY)
    startX = -smallestX
    startY = (largestY + -smallestY) + smallestY
    print("Start:",startX,startY)
    grid = createGrid(largestY + -smallestY + 1, largestX + -smallestX + 1)
    grid[startY][startX] = "s"
    #showGrid(grid)
    return grid, startY, startX

def isHorizontal(coords:list)->bool:    # Returns true if values in 2-d array coords represent a horizontal line
    return coords[0][1] == coords[1][1] 

def isVertical(coords:list)->bool:    # Returns true if values in 2-d array coords represent a vertical line
    return coords[0][0] == coords[1][0]

def partOne() -> int:       # Return the positions of the tail of the rope (moves like snake game)
    global lines
    grid, y, x = findGridSize()
    s = {"X":x,"Y":y}
    h = {"X":x,"Y":y}
    t = {"X":x,"Y":y}
    rope = [h,t]
    for line in lines:
        direction = line.split(" ")[0]
        amount = int(line.split(" ")[1])
        for count in range(amount):
            #grid[h["Y"]][h["X"]] = "."
            h = rope[0]
            if direction == "R":
                h["X"] += 1
            elif direction == "L":
                h["X"] -= 1
            elif direction == "U":
                h["Y"] -= 1
            elif direction == "D":
                h["Y"] += 1
            for ropePart in range(1,len(rope)):
                h = rope[ropePart-1]
                t = rope[ropePart]     
                #grid[h["Y"]][h["X"]] = "H"
                xDiff = h["X"] - t["X"]
                yDiff = h["Y"] - t["Y"]
                #print("XDiff:", xDiff, "YDiff:", yDiff)
                if (xDiff > 1 or xDiff < -1) or (yDiff > 1 or yDiff < -1): # time to move the tail
                    if isHorizontal([[t["X"],t["Y"]],[h["X"],h["Y"]]]):
                        if h["X"] > t["X"]:
                            t["X"] += 1
                        else:
                            t["X"] -= 1
                    elif isVertical([[t["X"],t["Y"]],[h["X"],h["Y"]]]):
                        if h["Y"] > t["Y"]:
                            t["Y"] += 1
                        else:
                            t["Y"] -= 1
                    else:
                        if yDiff < -1:
                            t["Y"] += yDiff +1
                            if xDiff > 0:
                                t["X"] += 1
                            else:
                                t["X"] += -1
                        elif yDiff > 1:
                            t["Y"] += yDiff -1
                            if xDiff > 0:
                                t["X"] += 1
                            else:
                                t["X"] += -1
                        elif xDiff > 1:
                            if yDiff > 0:
                                t["Y"] += 1
                            else:
                                t["Y"] += -1
                            t["X"] += xDiff -1
                        elif xDiff < -1:
                            if yDiff > 0:
                                t["Y"] += 1
                            else:
                                t["Y"] += -1
                            t["X"] += xDiff +1   
                if ropePart == 1:             
                    grid[t["Y"]][t["X"]] = ropePart
    #showGrid(grid)
    visitedCount = 0
    for row in grid:
        for x in row:
            if x == 1:
                visitedCount += 1
    return visitedCount

def partTwo() -> int:   # Return the sum of positions of the tail for a 10-part rope, like snake it consists of 1 head and 9 tails each following each other.
    global lines
    grid, y, x = findGridSize()
    s = {"X":x,"Y":y}
    h = {"X":x,"Y":y}
    one = {"X":x,"Y":y}
    two = {"X":x,"Y":y}
    three = {"X":x,"Y":y}
    four = {"X":x,"Y":y}
    five = {"X":x,"Y":y}
    six = {"X":x,"Y":y}
    seven = {"X":x,"Y":y}
    eight = {"X":x,"Y":y}
    nine = {"X":x,"Y":y}
    rope = [h,one,two,three,four,five,six,seven,eight,nine]
    for line in lines:
        direction = line.split(" ")[0]
        amount = int(line.split(" ")[1])
        for count in range(amount):
            #grid[h["Y"]][h["X"]] = "."
            h = rope[0]
            if direction == "R":
                h["X"] += 1
            elif direction == "L":
                h["X"] -= 1
            elif direction == "U":
                h["Y"] -= 1
            elif direction == "D":
                h["Y"] += 1
            for ropePart in range(1,len(rope)):
                h = rope[ropePart-1]
                t = rope[ropePart]
                
                #grid[h["Y"]][h["X"]] = "H"
                xDiff = h["X"] - t["X"]
                yDiff = h["Y"] - t["Y"]
                #print("XDiff:", xDiff, "YDiff:", yDiff)
                if (xDiff > 1 or xDiff < -1) or (yDiff > 1 or yDiff < -1): # time to move the tail
                    if isHorizontal([[t["X"],t["Y"]],[h["X"],h["Y"]]]):
                        if h["X"] > t["X"]:
                            t["X"] += 1
                        else:
                            t["X"] -= 1
                    elif isVertical([[t["X"],t["Y"]],[h["X"],h["Y"]]]):
                        if h["Y"] > t["Y"]:
                            t["Y"] += 1
                        else:
                            t["Y"] -= 1
                    else:
                        if yDiff < -1:
                            t["Y"] += yDiff +1
                            if xDiff > 0:
                                t["X"] += 1
                            else:
                                t["X"] += -1
                        elif yDiff > 1:
                            t["Y"] += yDiff -1
                            if xDiff > 0:
                                t["X"] += 1
                            else:
                                t["X"] += -1
                        elif xDiff > 1:
                            if yDiff > 0:
                                t["Y"] += 1
                            else:
                                t["Y"] += -1
                            t["X"] += xDiff -1
                        elif xDiff < -1:
                            if yDiff > 0:
                                t["Y"] += 1
                            else:
                                t["Y"] += -1
                            t["X"] += xDiff +1   
                if ropePart == 9:             
                    grid[t["Y"]][t["X"]] = ropePart
    #showGrid(grid)
    visitedCount = 0
    for row in grid:
        for x in row:
            if x == 9:
                visitedCount += 1
    return visitedCount

tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 2:", partTwo())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()