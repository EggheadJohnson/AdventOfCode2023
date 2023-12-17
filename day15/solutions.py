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

def getHashVal(word):
    val = 0
    for c in word:
        val += ord(c)
        val *= 17
        val %= 256
    return val

def part1(input):
    input = input[0]
    total = 0
    for word in input.split(','):
        val = getHashVal(word)
        debug("{}: {}".format(word, val))
        total += val
    return total

def removeLens(array, word):
    for i, lens in enumerate(array):
        if lens[0] == word:
            return array[:i] + array[i+1:]
    return array

def addLens(array, word, lensFactor):
    for i, lens in enumerate(array):
        if lens[0] == word:
            array[i] = (word, lensFactor)
            return array
    array.append((word, lensFactor))
    return array

def part2(input):
    total = 0
    input = input[0]
    array = [ [] for i in range(256) ]
    for word in input.split(','):
        if '-' in word:
            word = word[:-1]
            val = getHashVal(word)
            array[val] = removeLens(array[val], word)
        else:
            word, lensFactor = word.split('=')
            val = getHashVal(word)
            lensFactor = int(lensFactor)
            array[val] = addLens(array[val], word, lensFactor)
        debug([ box for box in array if len(box) > 0])
    for i, box in enumerate(array):
        for j, lens in enumerate(box):
            total += (i+1) * (j+1) * lens[1]
    return total
