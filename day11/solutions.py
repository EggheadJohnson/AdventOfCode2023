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

def findGalaxies(input):
    galaxies = {} # key original location to computed location
    for i, row in enumerate(input):
        for j, v in enumerate(row):
            if v == "#":
                galaxies[(i, j)] = [i, j]
    return galaxies

def part1(input):
    total = 0
    galaxies = findGalaxies(input)
    debug(galaxies)
    addSpace = 0
    for i, row in enumerate(input):
        debug(row)
        if '#' not in row:
            addSpace += 1
        else:
            for j, v in enumerate(row):
                if v == '#':
                    galaxies[(i, j)][0] += addSpace
    addSpace = 0
    for j, col in enumerate([ [ row[i] for row in input ] for i in range(len(input)) ]):
        debug(col)
        if '#' not in col:
            addSpace += 1
        else:
            for i, v in enumerate(col):
                if v == '#':
                    galaxies[(i, j)][1] += addSpace
    galaxyList = list(galaxies.keys())
    for i, galaxyA in enumerate(galaxyList[:-1]):
        for galaxyB in galaxyList[i+1:]:
            total += (abs(galaxies[galaxyA][0] - galaxies[galaxyB][0])) + (abs(galaxies[galaxyA][1] - galaxies[galaxyB][1]))

    return total

def part2(input):
    total = 0
    galaxies = findGalaxies(input)
    debug(galaxies)
    addSpace = 0
    expansion = 999999
    for i, row in enumerate(input):
        debug(row)
        if '#' not in row:
            addSpace += expansion
        else:
            for j, v in enumerate(row):
                if v == '#':
                    galaxies[(i, j)][0] += addSpace
    addSpace = 0
    for j, col in enumerate([ [ row[i] for row in input ] for i in range(len(input)) ]):
        debug(col)
        if '#' not in col:
            addSpace += expansion
        else:
            for i, v in enumerate(col):
                if v == '#':
                    galaxies[(i, j)][1] += addSpace
    galaxyList = list(galaxies.keys())
    for i, galaxyA in enumerate(galaxyList[:-1]):
        for galaxyB in galaxyList[i+1:]:
            total += (abs(galaxies[galaxyA][0] - galaxies[galaxyB][0])) + (abs(galaxies[galaxyA][1] - galaxies[galaxyB][1]))

    return total

