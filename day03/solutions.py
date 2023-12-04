import pprint, sys
sys.path.append('../python_utils')
from math import prod

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)

#############
#
# Results:
# result Part 1: 556367
# result Part 2: 89471771
#
#############

def isANumber(i):
    return i in '01234456789'

def getWholeNumber(board, pos):
    start = pos[1]
    while isANumber(board[pos[0]][start]):
        start -= 1
    start += 1
    end = pos[1]
    while end < len(board[pos[0]]) and isANumber(board[pos[0]][end]):
        end += 1
    return int(board[pos[0]][start:end])

def transformBoard(board):
    outputBoard = []
    for i, row in enumerate(board):
        newRow = []
        for j, c in enumerate(row):
            if isANumber(c):
                newRow.append(getWholeNumber(board, (i, j)))
            elif c == '.':
                newRow.append(0)
            else:
                newRow.append(c)
        outputBoard.append(newRow)
    return outputBoard
            

def part1(input):
    total = 0
    board = Board2D(input)
    for i, row in enumerate(board.board):
        currNum = 0
        shouldAdd = False
        for j, c in enumerate(row):
            if isANumber(c):
                currNum *= 10
                currNum += int(c)
                for pos in board.getNineSpotsCenteredAtPos((i, j)):
                    if board.isPositionInBoard(pos) and not isANumber(board.getPosition(pos)) and board.getPosition((pos)) != '.':
                        shouldAdd = True
            if currNum > 0 and (not isANumber(c) or j == len(row) - 1):
                if shouldAdd:
                    total += currNum
                currNum = 0
                shouldAdd = False

    

    return total

def safeIsNum(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def getDistinctNeighborNums(board, positions):
    grouped = [ positions[i:i+3] for i in range(0, 9, 3) ]
    nums = []
    currNum = None
    for group in grouped:
        group = [ board.getPosition(p) for p in group if board.isPositionInBoard(p)]
        for pos in group:
            if (not safeIsNum(pos) or pos == 0) and currNum is not None:
                nums.append(currNum)
                currNum = None
            elif currNum is None and safeIsNum(pos) and pos != 0:
                currNum = pos
        if currNum is not None:
            nums.append(currNum)
            currNum = None
    return nums
def part2(input):
    total = 0
    board = Board2D(transformBoard(input))
    for i, row in enumerate(board.board):
        for j, v in enumerate(row):
            if v == '*':
                neighbors = getDistinctNeighborNums(board, board.getNineSpotsCenteredAtPos((i, j)))
                if len(neighbors) == 2:
                    total += prod(neighbors)
    return total
