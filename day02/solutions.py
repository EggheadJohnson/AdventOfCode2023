import pprint, sys
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)

#############
#
# Results:
# 
# 
#
#############

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def parseLine(line):
    line = line.split(': ')[1]
    output = []
    for roll in line.split('; '):
        parsedRoll = {}
        for dice in roll.split(', '):
            dice = dice.strip()
            num, color = dice.split(' ')
            num = int(num)
            parsedRoll[color] = num
        output.append(parsedRoll)
    return output

def getLineNumber(line):
    return int(line.split(': ')[0].split(' ')[1])

# 1951 too low
def part1(input):
    redMax = 12
    greenMax = 13
    blueMax = 14
    total = 0
    for line in input:
        parsed = parseLine(line)
        valid = True
        for roll in parsed:
            if 'red' in roll and roll['red'] > redMax:
                valid = False
                break
            if 'green' in roll and roll['green'] > greenMax:
                valid = False
                break
            if 'blue' in roll and roll['blue'] > blueMax:
                valid = False
                break
        if valid:
            total += getLineNumber(line)
    return total

def part2(input):
    total = 0
    for line in input:
        parsed = parseLine(line)
        valid = True
        colorMins = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for roll in parsed:
            for color in roll:
                if roll[color] > colorMins[color]:
                    colorMins[color] = roll[color]
        total += colorMins['red'] * colorMins['green'] * colorMins['blue']
    return total
