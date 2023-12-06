import os, argparse, config, logging
from pprint import pformat
from datetime import *

parser = argparse.ArgumentParser()
parser.add_argument('--puzzle', action='store_true', help='Use the live puzzle data')
parser.add_argument('--debug', action='store_true', help='Print debug statements')
parser.add_argument('--time', action='store_true', help='Include execution time')
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)

def debug(*args):
    debugStr = ""
    for i in range(len(args)):
        logging.debug(pformat(args[i]))

config.debug = debug

file_path = os.path.dirname(os.path.realpath(__file__))
file_name = '/sample.txt'
if args.puzzle:
    file_name = '/puzzle.txt'
input_path = file_path + file_name

print('Opening {}'.format(file_name))

inpt = [ line.strip() for line in open(input_path, 'r')]

from solutions import part1, part2, part2b
if args.time:
    pt1Start = datetime.now()
    pt1Result = part1(inpt)
    pt1End = datetime.now()
    print("result Part 1: {} time: {}.{}".format(pt1Result, (pt1End - pt1Start).seconds, (pt1End - pt1Start).microseconds))
    pt2Start = datetime.now()
    pt2Result = part2(inpt)
    pt2End = datetime.now()
    print("result Part 2: {} time: {}.{}".format(pt2Result, (pt2End - pt2Start).seconds, (pt2End - pt2Start).microseconds))
    pt3Start = datetime.now()
    pt3Result = part2b(inpt)
    pt3End = datetime.now()
    print("result Part 2b: {} time: {}.{}".format(pt3Result, (pt3End - pt3Start).seconds, (pt3End - pt3Start).microseconds))
else:
    print("result Part 1:", part1(inpt))
    print("result Part 2:", part2(inpt))
    print("result Part 2b:", part2b(inpt))
