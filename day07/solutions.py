import pprint, sys, config
from functools import cmp_to_key
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

def compareCards(a, b):
    cardRanks = 'AKQJT98765432'
    if a['handType'] != b['handType']:
        return a['handType'] - b['handType']
    for i in range(5):
        if a['hand'][i] != b['hand'][i]:
            return cardRanks.index(a['hand'][i]) - cardRanks.index(b['hand'][i])

def compareCardsPtDeux(a, b):
    cardRanks = 'AKQT98765432J'
    if a['handType'] != b['handType']:
        return a['handType'] - b['handType']
    for i in range(5):
        if a['hand'][i] != b['hand'][i]:
            return cardRanks.index(a['hand'][i]) - cardRanks.index(b['hand'][i])

def sortCards(cardList, compareCards=compareCards):
    return sorted(cardList, reverse=True, key=cmp_to_key(compareCards))

# 0 Five of a kind, where all five cards have the same label: AAAAA
# 1 Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# 2 Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# 3 Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# 4 Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# 5 One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# 6 High card, where all cards' labels are distinct: 23456
def getHandType(cc):
    if len(cc.keys()) == 1:
        return 0
    if len(cc.keys()) == 2:
        if 4 in cc.values():
            return 1
        else:
            return 2
    if len(cc.keys()) == 3:
        if 3 in cc.values():
            return 3
        else:
            return 4
    if len(cc.keys()) == 4:
        return 5
    return 6

def getHandTypePtDeux(cc):
    if len(cc.keys()) == 1:
        return 0
    if len(cc.keys()) == 2:
        if 'J' in cc:
            return 0
        if 4 in cc.values():
            return 1
        else:
            return 2
    if len(cc.keys()) == 3:
        if 3 in cc.values():
            if 'J' in cc:
                return 1
            return 3
        else:
            if 'J' in cc and cc['J'] == 2:
                return 1
            elif 'J' in cc and cc['J'] == 1:
                return 2
            return 4
    if len(cc.keys()) == 4:
        if 'J' in cc:
            return 3
        return 5
    if 'J' in cc:
        return 5
    return 6

def parseLine(line, getHandType=getHandType):
    hand, score = line.split(' ')
    cardCounts = {}
    handTypes = [
        'five-of-a-kind',
        'four-of-a-kind',
        'full-house',
        'three-of-a-kind',
        'two-pair',
        'one-pair',
        'high-card',
    ]
    for card in set(hand):
        cardCounts[card] = hand.count(card)
    return {
        'hand': hand,
        'score': int(score),
        'cardCounts': cardCounts,
        'handType': getHandType(cardCounts),
        'handTypeReadable': handTypes[getHandType(cardCounts)]
    }

def part1(input):
    total = 0
    game = [ parseLine(hand) for hand in input ]
    sortedGame = sortCards(game)
    debug(sortedGame)
    for i, c in enumerate(sortedGame):
        total += (c['score'] * (i+1))
    return total

def part2(input):
    total = 0
    game = [ parseLine(hand, getHandTypePtDeux) for hand in input ]
    sortedGame = sortCards(game, compareCardsPtDeux)
    debug(sortedGame)
    mostJ = 0
    for hand in game:
        if 'J' in hand['hand']:
            if hand['hand'].count('J') > mostJ:
                mostJ = hand['hand'].count('J')
            debug('part2 {} {}'.format(hand['hand'], hand['handTypeReadable']))
    debug(len([ h for h in game if 'J' in h['hand']]))
    debug(mostJ)
    for i, c in enumerate(sortedGame):
        total += (c['score'] * (i+1))
    return total
