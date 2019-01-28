import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
args = parser.parse_args()

if len(args.arg) < 1:
    sys.stdout.write('no args')
else:
    sys.stdout.write('\n'.join(args.arg))
