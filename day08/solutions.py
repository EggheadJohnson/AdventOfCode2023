import pprint, sys, config
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra
from math import sqrt

pp = pprint.PrettyPrinter(indent=4)
debug = config.debug

#############
#
# Results:
# result Part 1: 20659
# result Part 2: 15690466351717
#
#############

def parseAndBuildMap(mapIn):
    mapOut = {}
    for line in mapIn:
        loc, dirs = line.split(' = ')
        l, r = dirs[1:-1].split(', ')
        mapOut[loc] = {
            'L': l,
            'R': r
        }
    return mapOut

def takeAWalk(steps, puzzMap, loc='AAA', version=1):
    i = 0
    if version == 1:
        while loc != 'ZZZ':
            loc = puzzMap[loc][steps[i % len(steps)]]
            i += 1
    else:
        while loc[-1] != 'Z':
            loc = puzzMap[loc][steps[i % len(steps)]]
            i += 1
    return i

def takeMultipleWalks(steps, puzzMap):
    locs = getSpotsEndingInA(puzzMap)
    i = 0
    while len([ l for l in locs if l[-1] == 'Z']) != len(locs):
        locs = [ puzzMap[l][steps[i%len(steps)]] for l in locs ]
        debug(locs)
        i += 1
    return i

def primeFact(n):
    c = n
    pf = []
    while c > 1:
        for x in range(2, c+1):
            if c % x == 0:
                pf.append(x)
                c //= x
                break
    return pf
    


def getSpotsEndingInA(puzzMap):
    return [ k for k in puzzMap.keys() if k[-1] == 'A']

def getSpotsEndingInZ(puzzMap):
    return [ k for k in puzzMap.keys() if k[-1] == 'Z']

def part1(input):
    steps = input[0]
    puzzMap = parseAndBuildMap(input[2:])
    return takeAWalk(steps, puzzMap)

def part2(input):
    steps = input[0]
    puzzMap = parseAndBuildMap(input[2:])
    checkSpots = getSpotsEndingInA(puzzMap)
    debug(checkSpots)
    total = 283
    for spot in checkSpots:
        walkLen = takeAWalk(steps, puzzMap, spot, 2) # it turned out that the '..Z' spots would occur at regular intervals
        debug(spot, walkLen, primeFact(walkLen))
        facts = primeFact(walkLen)
        debug(facts[0])
        total *= facts[0]
    return total