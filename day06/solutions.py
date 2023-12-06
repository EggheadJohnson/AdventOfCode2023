import pprint, sys, config, re
from math import sqrt, ceil, floor
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)
debug = config.debug

#############
#
# Results:
# result Part 1: 345015 time: 0.225
# result Part 2: 42588603 time: 0.498503
# result Part 2b: 42588603 time: 0.140
#
#############

def parseInput(input):
    times = [ int(i) for i in re.split(r'\s+', input[0][6:].strip())]
    dists = [ int(i) for i in re.split(r'\s+', input[1][9:].strip())]
    debug(times, dists)
    return list(zip(times, dists))

def part1(input):
    total = 1
    timeDists = parseInput(input)
    for time, dist in timeDists:
        wins = [ i*(time-i) for i in range(time+1) if i*(time-i) > dist ]
        debug(wins)
        total *= len(wins)
    return total

def part2(input):
    timeDists = parseInput(input)
    time = int(''.join([str(i[0]) for i in timeDists]))
    dist = int(''.join([str(i[1]) for i in timeDists]))
    debug('pt2', time, dist)
    i = 0
    while i*(time-i) < dist:
        i += 1
    debug(i, time, 1+time-(2*i))
    
    return 1+time-(2*i)

def part2b(input):
    timeDists = parseInput(input)
    time = int(''.join([str(i[0]) for i in timeDists]))
    dist = int(''.join([str(i[1]) for i in timeDists]))

    debug((-1*time + sqrt(time**2 - 4*(-1)*(-1*dist))) / (2*-1))
    debug((-1*time - sqrt(time**2 - 4*(-1)*(-1*dist))) / (2*-1))
    boundaries = ((-1*time + sqrt(time**2 - 4*(-1)*(-1*dist))) / (2*-1), (-1*time - sqrt(time**2 - 4*(-1)*(-1*dist))) / (2*-1))
    return 1+ floor(max(boundaries)) - ceil(min(boundaries))