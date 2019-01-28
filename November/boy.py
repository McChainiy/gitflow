import argparse
import sys

converter = {'football': 100, 'other': 50, 'melodrama': 0}

parser = argparse.ArgumentParser()

parser.add_argument('--barbie', default=50, type=int)
parser.add_argument('--cars', default=50, type=int)
parser.add_argument('--movie', default='other')

args = parser.parse_args()

args.barbie = args.barbie if args.barbie in range(101) else 50
args.cars = args.cars if args.cars in range(101) else 50

boy_coef = int((100 - args.barbie + args.cars + converter[args.movie]) / 3)
sys.stdout.write('boy: {}\n'.format(boy_coef))
sys.stdout.write('girl: {}'.format(100 - boy_coef))