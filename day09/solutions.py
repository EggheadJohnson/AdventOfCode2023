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

def getNextSeq(seq):
    return [ seq[i] - seq[i-1] for i in range(1, len(seq)) ]

def getToDeltaZeros(line, reverse=False):
    curr = [ int(n) for n in line.split(' ')]
    seq = [ curr ]
    next = getNextSeq(curr)
    seq.append(next)
    while len([ i for i in next if i != 0]):
        curr = next[:]
        next = getNextSeq(curr)
        seq.append(next)
    if reverse:
        for line in seq:
            line.reverse()
    return seq

def getNextVal(seq):
    seq[-1].append(0)
    for i in range(len(seq)-2, -1, -1):
        seq[i].append(seq[i][-1] + seq[i+1][-1])
    debug(seq)
    return seq[0][-1]

def getPrevVal(seq):
    seq[-1].append(0)
    for i in range(len(seq)-2, -1, -1):
        seq[i].append(seq[i][-1] - seq[i+1][-1])
    debug(seq)
    return seq[0][-1]

def part1(input):
    total = 0
    for line in input:
        seq = getToDeltaZeros(line)
        total += getNextVal(seq)
    return total

def part2(input):
    total = 0
    for line in input:
        seq = getToDeltaZeros(line, True)
        debug(seq)
        total += getPrevVal(seq)
    return total
