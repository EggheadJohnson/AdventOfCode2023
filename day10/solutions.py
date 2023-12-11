import pprint, sys, config
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)
debug = config.debug

#############
#
# Results:
#
#
#
#############

def findStart(board):
    for i, line in enumerate(board.board):
        for j, c in enumerate(line):
            if c == 'S':
                return (i, j)



def findTwoPointingAtStart(board, start):
    options = board.getAdjacentPositions(start)
    connections = []
    for spot in options:
        debug(spot, board.getPosition(spot))
        if spot[0] < start[0]: # above
            if board.getPosition(spot) in "|7F":
                connections.append(spot)
        elif spot[0] > start[0]: # below
            if board.getPosition(spot) in "|LJ":
                connections.append(spot)
        elif spot[1] < start[1]: # left
            if board.getPosition(spot) in "-LF":
                connections.append(spot)
        elif spot[1] > start[1]: # right
            if board.getPosition(spot) in "-J7":
                connections.append(spot)

    return connections

def getPosExit(board, pos, prev):
    shape = board.getPosition(pos)
    if pos[0] < prev[0]: # moved up
        if shape == '|':
            return (pos[0] - 1, pos[1])
        if shape == '7':
            return (pos[0], pos[1] - 1)
        if shape == 'F':
            return (pos[0], pos[1] + 1)
    if pos[0] > prev[0]: # moved down
        if shape == '|':
            return (pos[0]+1, pos[1])
        if shape == 'L':
            return (pos[0], pos[1]+1)
        if shape == 'J':
            return (pos[0], pos[1]-1)
    if pos[1] > prev[1]: # moved right
        if shape == '-':
            return (pos[0], pos[1]+1)
        if shape == 'J':
            return (pos[0]-1, pos[1])
        if shape == '7':
            return (pos[0]+1, pos[1])
    if pos[1] < prev[1]:
        if shape == '-':
            return (pos[0], pos[1]-1)
        if shape == 'L':
            return (pos[0]-1, pos[1])
        if shape == 'F':
            return (pos[0]+1, pos[1])


def mapPipe(board, start):
    a, _ = findTwoPointingAtStart(board, start)
    pipe = set()
    pipe.add(start)
    prevA = start
    while a not in pipe:
        pipe.add(a)
        temp = a
        a = getPosExit(board, a, prevA)
        prevA = temp

    return pipe


def part1(input):
    # debug(*input)
    board = Board2D(input)
    start = findStart(board)
    debug(start)
    a, b = findTwoPointingAtStart(board, start)
    debug(a, b)
    seenA = set()
    seenA.add(a)
    c = 1 # starting 1 step away from start
    aPrev = start
    bPrev = start
    while b not in seenA:
        temp = a
        a = getPosExit(board, a, aPrev)
        aPrev = temp
        seenA.add(a)
        temp = b
        b = getPosExit(board, b, bPrev)
        bPrev = temp
        c += 1


    return c

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

def printInColor(board, pipe, inside):
    P = "\033[1;31mP\033[0m"
    I = "\033[1;32mI\033[0m"
    o = '.'
    for i in range(len(board.board)):
        line = ''
        for j in range(len(board.board[i])):
            if (i, j) in pipe:
                line += P
            elif (i, j) in inside:
                line += I
            else:
                line += o
        print(line)

# 440 is too high
def part2(input):
    board = Board2D(input)
    start = findStart(board)
    startShape = '|' # only works for puzzle, TODO: refactor for general solution
    board.setPosition(start, startShape)
    debug(start)
    pipe = mapPipe(board, start)
    insideCount = 0
    inside = set()
    for i, line in enumerate(board.board):
        passedPipes = 0
        prevCorner = None
        for j, c in enumerate(line):

            if (i, j) in pipe:
                if c in '|':
                    passedPipes += 1
                elif c in 'LF':
                    passedPipes += 1
                    prevCorner = c
                elif c in 'J7':
                    if c == 'J' and prevCorner == 'L':
                        passedPipes += 1
                    elif c == '7' and prevCorner == 'F':
                        passedPipes += 1
                    prevCorner = None

            else:
                if passedPipes % 2 == 1:
                    insideCount += 1
                    inside.add((i, j))
    # printInColor(board, pipe, inside)
    return insideCount
