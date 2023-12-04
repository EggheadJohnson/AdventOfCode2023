import os, argparse, config, logging

parser = argparse.ArgumentParser()
parser.add_argument('--puzzle', action='store_true', help='Use the live puzzle data')
parser.add_argument('--debug', action='store_true', help='Print debug statements')
args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)

def debug(*args):
    debugStr = ""
    for i in range(len(args)):
        debugStr += " {}"
    logging.debug(debugStr.format(*args))

config.debug = debug

file_path = os.path.dirname(os.path.realpath(__file__))
file_name = '/sample.txt'
if args.puzzle:
    file_name = '/puzzle.txt'
input_path = file_path + file_name

print('Opening {}'.format(file_name))

inpt = [ line.strip() for line in open(input_path, 'r')]

from solutions import part1, part2
print("result Part 1:", part1(inpt))
print("result Part 2:", part2(inpt))
