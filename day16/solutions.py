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

def getSpots(board, pos, dir):
    char = board.getPosition(pos)
    res = []
    if char == '.':
        res = [((pos[0]+dir[0], pos[1]+dir[1]), dir)]
    if char == '-':
        if dir[1] == 1 or dir[1] == -1:
            res = [((pos[0], pos[1] + dir[1]), dir)]
        else:
            res = [((pos[0], pos[1]-1), (0, -1)), ((pos[0], pos[1]+1), (0, 1))]
    if char == '|':
        if dir[0] == 1 or dir[0] == -1:
            res = [((pos[0]+dir[0], pos[1]), dir)]
        else:
            res = [((pos[0]-1, pos[1]), (-1, 0)), ((pos[0]+1, pos[1]), (1, 0))]
    if char == '/':
        if dir[0] == 1:
            res = [( (pos[0], pos[1]-1), (0, -1) )]
        if dir[0] == -1:
            res = [( (pos[0], pos[1]+1), (0, 1) )]
        if dir[1] == 1:
            res = [( (pos[0]-1, pos[1]), (-1, 0) )]
        if dir[1] == -1:
            res = [( (pos[0]+1, pos[1]), (1, 0) )]
    if char == '\\':
        if dir[0] == 1:
            res = [( (pos[0], pos[1]+1), (0, 1) )]
        if dir[0] == -1:
            res = [( (pos[0], pos[1]-1), (0, -1) )]
        if dir[1] == 1:
            res = [( (pos[0]+1, pos[1]), (1, 0) )]
        if dir[1] == -1:
            res = [( (pos[0]-1, pos[1]), (-1, 0) )]
    # debug(res)
    res = [ pos for pos in res if board.isPositionInBoard(pos[0]) ]
    return res

def part1(input, startingPosDir = ((0, 3), (1, 0))):
    board = Board2D(input)
    posDir = startingPosDir
    posDirQueue = getSpots(board, posDir[0], posDir[1])
    seen = set()
    seen.add(posDir)
    while len(posDirQueue) > 0:
        posDir = posDirQueue.pop()
        seen.add(posDir)
        newSpots = getSpots(board, posDir[0], posDir[1])
        newSpots = [ spot for spot in newSpots if spot not in seen ]
        posDirQueue.extend(newSpots)

    return len(set([ posDir[0] for posDir in seen ]))

def part2(input):
    board = Board2D(input)
    maxVal = 0
    for j in range(len(board.board[0])):
        bot = len(board.board) - 1
        val = part1(input, ( (0, j), (1, 0)))
        if val > maxVal:
            maxVal = val
            debug("Updating maxVal to {}".format(val))
        val = part1(input, ( (bot, j), (-1, 0)))
        if val > maxVal:
            maxVal = val
            debug("Updating maxVal to {}".format(val))
    for i in range(len(board.board)):
        right = len(board.board[0]) - 1
        val = part1(input, ( (i, 0), (0, 1)))
        if val > maxVal:
            maxVal = val
            debug("Updating maxVal to {}".format(val))
        val = part1(input, ( (i, right), (0, -1)))
        if val > maxVal:
            maxVal = val
            debug("Updating maxVal to {}".format(val))
    return maxVal
