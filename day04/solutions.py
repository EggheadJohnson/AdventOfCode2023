import pprint, sys
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)

#############
#
# Results:
# result Part 1: 18653
# result Part 2: 5921508
#
#############

def parseCard(card, debug):
    cardNum = card.split(': ')[0].split(' ')[1]
    winners, cards = card.split(': ')[1].split(' | ')
    winners = set([ int(v) for v in winners.strip().split(' ') if len(v) > 0])
    cards = set([ int(v) for v in cards.strip().split(' ') if len(v) > 0 ])
    return winners, cards

def part1(input, debug):
    total = 0
    for line in input:
        winners, cards = parseCard(line, debug)
        debug(winners & cards, len(winners & cards))
        if len(winners & cards) > 0:
            total += 2**(len(winners & cards) - 1)
    return total

def part2(input, debug):
    copies = []
    for x in range(len(input)):
        copies.append(1)
    for i, card in enumerate(input):
        winners, cards = parseCard(card, debug)
        for x in range(len(winners & cards)):
            copies[i+x+1] += copies[i]
    debug(copies)
    return sum(copies)
