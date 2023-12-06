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

def getSeeds(line):
    return [ int(seed) for seed in line.split(': ')[1].split(' ') ]

def segmentInputIntoBlocks(input):
    allBlocks = []
    block = []
    for line in input:
        if len(line) == 0:
            allBlocks.append(block)
            block = []
        else:
            block.append(line)
    allBlocks.append(block)
    return allBlocks

def parseBlock(block):
    name = block[0].split(' ')[0].split('-to-')
    lines = [ [int(n) for n in line.split(' ')] for line in block[1:] ]
    blockMap = []
    for line in lines:
        blockMap.append( ((line[1], line[1]+line[2]-1), line[0]) )
    blockMap = list(sorted(blockMap, key=lambda b: b[0][0]))
    return name, blockMap

def binSearchForBlock(blockMap, val):
    lowerBound = 0
    upperBound = len(blockMap)
    if val < blockMap[0][0][0]:
        return -1
    if val > blockMap[-1][0][1]:
        return -1
    while True:
        if upperBound - lowerBound < 2:
            if val >= blockMap[lowerBound][0][0] and val <= blockMap[lowerBound][0][1]:
                return lowerBound
            elif val >= blockMap[upperBound][0][0] and val <= blockMap[upperBound][0][1]:
                return upperBound
            else:
                return -1
        i = (upperBound - lowerBound) // 2
        block = blockMap[lowerBound + i][0]
        if val >= block[0] and val <= block[1]:
            return lowerBound + i
        if val < block[0]:
            upperBound = lowerBound + i
        elif val > block[1]:
            lowerBound = lowerBound + i

def areThereBreaks(blockMap):
    for i, block in enumerate(blockMap[:-1]):
        if block[0][1] + 1 < blockMap[i+1][0][0]:
            return True
    return False

def mapSeedToLocation(maps, seed):
    point = 'seed'
    step = seed
    while point != 'location':
        # debug((point, step))
        block = binSearchForBlock(maps[point]['block'], step)
        if block != -1:
            block = maps[point]['block'][block]
            step = block[1] + (step - block[0][0])
        point = maps[point]['dest']
        # debug(step)
    return step

def part1(input):
    seeds = getSeeds(input[0])
    debug(seeds)
    segmented = segmentInputIntoBlocks(input[2:])
    debug(segmented)
    maps = {}
    for block in segmented:
        name, sortedBlock = parseBlock(block)
        source, dest = name
        debug(source)
        block = {
            'source': source,
            'dest': dest,
            'block': sortedBlock
        }
        maps[source] = block
    debug(maps)
    # debug(binSearchForBlock(maps['soil']['block'], 14))
    # for key in maps:
    #     if areThereBreaks(maps[key]['block']):
    #         debug(key, areThereBreaks(maps[key]['block']))

    seedLocations = [ mapSeedToLocation(maps, seed) for seed in seeds ]
    debug(seedLocations)
    return min(seedLocations)

# def getPart2Seeds(seeds):


def part2(input):
    seeds = getSeeds(input[0])
    groupedSeeds = [ (seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2) ]
    debug(groupedSeeds)
    segmented = segmentInputIntoBlocks(input[2:])
    debug(segmented)
    maps = {}
    for block in segmented:
        name, sortedBlock = parseBlock(block)
        source, dest = name
        debug(source)
        block = {
            'source': source,
            'dest': dest,
            'block': sortedBlock
        }
        maps[source] = block
    debug(maps)
    # debug(binSearchForBlock(maps['soil']['block'], 14))
    # for key in maps:
    #     if areThereBreaks(maps[key]['block']):
    #         debug(key, areThereBreaks(maps[key]['block']))

    smallestLocation = None
    for pair in groupedSeeds:
        seedGroup = range(pair[0], pair[0]+pair[1])
        seedLocations = [ mapSeedToLocation(maps, seed) for seed in seedGroup ]
        groupMin = min(seedLocations)
        if smallestLocation is None or groupMin < smallestLocation:
            smallestLocation = groupMin
    
    return smallestLocation