import pprint, sys
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)

#############
#
# Results:
# 
# result Part 1: 55386
# result Part 2: 54824
#
#############

def isANumber(c):
    return c in '0123456789'

def fetchNumberFromLine(line):
    nums = []
    for c in line:
        if isANumber(c):
            nums.append(int(c))
    return 10*nums[0] + nums[-1]

def getNumFromName(name):
    numNames = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    return int(numNames[name])

def findFirstNum(line):
    firstNumeric = None
    numNames = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for i, c in enumerate(line):
        if isANumber(c):
            firstNumeric = i
            break
    firstNumName = None
    firstNumNameIndex = None
    for name in numNames:
        i = line.find(name)
        if i >= 0 and (firstNumName is None or i < firstNumNameIndex):
            firstNumName = name
            firstNumNameIndex = i
    if firstNumName is None:
        return int(line[firstNumeric])
    if firstNumeric is None:
        return getNumFromName(firstNumName)
    if firstNumeric < firstNumNameIndex:
        return int(line[firstNumeric])
    return getNumFromName(firstNumName)
    

def findLastNum(line):
    lastNumeric = None
    numNames = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(line)-1, -1, -1):
        if isANumber(line[i]):
            lastNumeric = i
            break
    lastNumName = None
    lastNumNameIndex = None
    for name in numNames:
        i = line.rfind(name)
        if i >= 0 and (lastNumName is None or i > lastNumNameIndex):
            lastNumName = name
            lastNumNameIndex = i
    if lastNumName is None:
        return int(line[lastNumeric])
    if lastNumeric is None:
        return getNumFromName(lastNumName)
    if lastNumeric > lastNumNameIndex:
        return int(line[lastNumeric])
    return getNumFromName(lastNumName)
    
def getNumberFromLine(line):
    return 10*findFirstNum(line) + findLastNum(line)

def part1(input):
    total = 0
    for line in input:
        lineNum = fetchNumberFromLine(line)
        total += lineNum
    return total

def part2(input):
    total = 0
    for line in input:
        total += getNumberFromLine(line)
    return total
