#
import time, tracemalloc    # Used for efficiency tracking of elapsed time and memory usage
lines = open("day-2-puzzle-input.txt","r").read().splitlines()

def partOne()->int: # Returns the score from rock, paper, scissors
    global lines
    score = 0
    ROCK = "AX"
    PAPER = "BY"
    SCISSORS = "CZ"
    WIN = 6
    DRAW = 3
    LOSE = 0
    for line in lines:
        myShape = line[2]
        elfShape = line[0]
        if myShape in ROCK:  
            score += 1
        elif myShape in PAPER:    
            score += 2
        elif myShape in SCISSORS:    
            score += 3
        if (elfShape in ROCK and myShape in PAPER) or \
             (elfShape in PAPER and myShape in SCISSORS) or \
             (elfShape in SCISSORS and myShape in ROCK):   
            score += WIN
        elif (elfShape in ROCK and myShape in ROCK) or \
             (elfShape in PAPER and myShape in PAPER) or \
             (elfShape in SCISSORS and myShape in SCISSORS): 
            score += DRAW
    return score

def partTwo()->int: # Returns the score from rock, paper, scissors
    global lines
    score = 0
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"
    PLAYWIN = "Z"
    PLAYDRAW = "Y"
    PLAYLOSE = "X"
    for line in lines:
        myShape = line[2]
        elfShape = line[0]
        if elfShape == ROCK and myShape == PLAYLOSE:     # Scissors
            score += 0 + 3
        elif elfShape == ROCK and myShape == PLAYWIN:   # Paper
            score += 6 + 2 
        elif elfShape == ROCK and myShape == PLAYDRAW:   # Rock
            score += 3 + 1
        elif elfShape == PAPER and myShape == PLAYWIN:  # Scissors
            score += 6 + 3
        elif elfShape == PAPER and myShape == PLAYDRAW:   # Paper
            score += 3 + 2
        elif elfShape == PAPER and myShape == PLAYLOSE:   # Rock
            score += 0 + 1
        elif elfShape == SCISSORS and myShape == PLAYDRAW:  # Scissors
            score += 3 + 3
        elif elfShape == SCISSORS and myShape == PLAYLOSE:   # Paper
            score += 0 + 2
        elif elfShape == SCISSORS and myShape == PLAYWIN:   # Rock
            score += 6 + 1
    return score

def partOneA()->int: # Returns the score from rock, paper, scissors, using dictionaries instead of selection
    global lines
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"
    POINTS = {
        (ROCK, ROCK) : 3,
        (ROCK, PAPER) : 6,
        (ROCK, SCISSORS): 0,
        (PAPER, PAPER) : 3,
        (PAPER, SCISSORS) : 6,
        (PAPER, ROCK): 0,
        (SCISSORS, SCISSORS) : 3,
        (SCISSORS, ROCK) : 6,
        (SCISSORS, PAPER): 0,
    }
    SHAPE = {
        "X": ROCK,
        "Y": PAPER,
        "Z": SCISSORS
    }
    SHAPE_POINT = {
        ROCK: 1,
        PAPER: 2,
        SCISSORS: 3
    }
    score = 0
    for line in lines:
        score += POINTS[(line[0],SHAPE[line[2]])] + SHAPE_POINT[SHAPE[line[2]]]
    return score

def partTwoA()->int: # Returns the score from rock, paper, scissors, using a dictionary instead of selection
    global lines
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"
    POINTS = {
        (ROCK, LOSE): 3,
        (ROCK, DRAW): 4,
        (ROCK, WIN) : 8,
        (PAPER, LOSE): 1,
        (PAPER, DRAW): 5,
        (PAPER, WIN) : 9,
        (SCISSORS, LOSE): 2,
        (SCISSORS, DRAW): 6,
        (SCISSORS, WIN): 7,
    }
    score = 0
    for line in lines:
        score += POINTS[(line[0], line[2])]
    return score


tracemalloc.start()     # Start memory allocation trace
start = time.time()
 
# Part One
print(partOneA())
# Part Two
print(partTwoA())

print("\t\tTotal elapsed time:", time.time()-start)
print("Memory Usage\tCurrent:",tracemalloc.get_traced_memory()[0],"\tPeak:",tracemalloc.get_traced_memory()[1])
tracemalloc.stop()
