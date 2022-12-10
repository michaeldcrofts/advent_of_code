#
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-10-puzzle-input.txt","r").read().splitlines()

def partOne() -> int:       # Return the signal strength of cycle*register for cycles 20,60,100,140,180,220
    global lines
    register = 1
    cycles = [1]
    for line in lines:
        if line[0:3] == "add":
            operand = int(line.split(" ")[1])
            cycles.append(register)
            register += operand
            cycles.append(register)
        else:
            cycles.append(register)
    totalSignal = 0
    for count in range(20,221,40):
        #print("Cycle:", count, "Register", cycles[count-1])
        totalSignal += count * cycles[count-1]
    return totalSignal

def partTwo():              # Print the CRT display for pixels to form a word
    global lines
    register = 1
    cycles = [1]
    for line in lines:
        if line[0:3] == "add":
            operand = int(line.split(" ")[1])
            cycles.append(register)
            register += operand
            cycles.append(register)
        else:
            cycles.append(register)
    # Part 2
    display = []
    for i in range(6):
        row = []
        for colCount in range(40):
            row.append(".")
        display.append(row)
    pixel = 0
    row = 0
    print(len(cycles))
    for cycle in cycles:
        spritePos = [cycle-1,cycle,cycle+1]
        if pixel in spritePos:
            display[row][pixel] = "#"
        pixel += 1
        if pixel > 39:
            pixel = 0
            row += 1
    for rowCount in range(len(display)):
        for colCount in range(len(display[rowCount])):
            print(display[rowCount][colCount],end="")
        print()
    print()



tracemalloc.start()     # Start memory allocation trace
start = time.time()

# Part One
print("Part 1:", partOne())
# Part Two
print("Part 2:", partTwo())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
