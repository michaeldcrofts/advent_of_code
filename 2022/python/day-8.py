#--- Day 8: Treetop Tree House ---
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-8-puzzle-input.txt","r").read().splitlines()

def createGrid() -> list:   # Return a 2-d array of integers from the data in lines.
    global lines
    grid = []
    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        grid.append(row)
    return grid

def showGrid(grid: list):   # Output a visualisation of the 2-d array, useful for debugging!
    for row in grid:
        for x in row:
            print(x,sep="",end="")
        print()

def partOne()->int:              # From a 2-d grid of 'trees', return a count of those that can be 'seen' from the perimeter
    grid = createGrid()
    #showGrid(grid)
    visible = (len(grid[0])-1)*2 + (len(grid)-1)*2  # perimeter
    for rCount in range(1,len(grid)-1):             # Iterate through each row
        for treeCount in range(1,len(grid[0])-1):   # Iterate through each tree in row
            north = []
            south = []
            west = []
            east = []
            for count in range(0, rCount):          # Make a list of 'trees' in the same column position for the rows above
                north.append(grid[count][treeCount])
    
            for count in range(rCount+1,len(grid)): # Make a list of 'trees' in the same column position for the rows below
                south.append(grid[count][treeCount])
            
            for count in range(0, treeCount):       # Make a list of 'trees' in the same row to the left
                west.append(grid[rCount][count])
            
            for count in range(treeCount+1, len(grid[rCount])): # Make a list of 'trees' in the same row to the right
                east.append(grid[rCount][count])
            # Check visibility
            northVis = southVis = eastVis = westVis = True
            for tree in north:
                if tree >= grid[rCount][treeCount]:
                    northVis = False
            for tree in south:
                if tree >= grid[rCount][treeCount]:
                    southVis = False
            for tree in east:
                if tree >= grid[rCount][treeCount]:
                    eastVis = False
            for tree in west:
                if tree >= grid[rCount][treeCount]:
                    westVis = False
            #print("Tree pos:", treeCount,"x",rCount, "=", grid[rCount][treeCount], "North:", north, "South:", south, "East:", east, "West:", west, "Visible:",northVis,eastVis,southVis,westVis)
            if northVis or southVis or eastVis or westVis:
                visible+=1
    return visible

def partTwo()->int:         # Return the highest scenic score, number of trees (multiplied) that can be seen from any one position
    grid = createGrid()
    #showGrid(grid)
    highest = 0
    for rCount in range(1,len(grid)-1):             # Iterate through each row
        for treeCount in range(1,len(grid[0])-1):   # Iterate through each tree in row
            north = []
            south = []
            west = []
            east = []
            for count in range(0, rCount):          # Make a list of 'trees' in the same column position for the rows above
                north.append(grid[count][treeCount])
            
            for count in range(rCount+1,len(grid)): # Make a list of 'trees' in the same column position for the rows below
                south.append(grid[count][treeCount])
            
            for count in range(0, treeCount):        # Make a list of 'trees' in the same row to the left
                west.append(grid[rCount][count])
            
            for count in range(treeCount+1, len(grid[rCount])): # Make a list of 'trees' in the same row to the right
                east.append(grid[rCount][count])

            # Calculate highest scenic score - the number of trees that can be seen from a single position multiplied
            north.reverse()    # Because we're outwards from the tree, rather than inward from the perimeter
            west.reverse()
            northVis = southVis = eastVis = westVis = 0
            for tree in north:
                if tree < grid[rCount][treeCount]:
                    northVis += 1
                else:
                    northVis += 1
                    break
            for tree in south:
                if tree < grid[rCount][treeCount]:
                    southVis += 1
                else:
                    southVis += 1
                    break
            for tree in east:
                if tree < grid[rCount][treeCount]:
                    eastVis += 1
                else:
                    eastVis += 1
                    break
            for tree in west:
                if tree < grid[rCount][treeCount]:
                    westVis += 1
                else:
                    westVis += 1
                    break
            #print("Tree pos:", treeCount,"x",rCount, "=", grid[rCount][treeCount], "North:", north, "West:", west, "East:", east, "South:", south,"Visible:",northVis,westVis,eastVis,southVis)
            view = northVis * westVis * southVis * eastVis
            if view > highest:
                highest = view
    return highest

tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 2:", partTwo())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()