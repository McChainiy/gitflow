import sys
import argparse

choice = {'day': 1, 'month': 30, 'year': 360}
perdun = 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--perday', type=int, default=0)
    parser.add_argument('--perweek', type=int, default=0)
    parser.add_argument('--permonth', type=int, default=0)
    parser.add_argument('--peryear', type=int, default=0)
    parser.add_argument('--getby', choices=['day', 'month', 'year'], default='day')
    args = parser.parse_args()
    kaef = int(args.perday + args.perweek / 7 + args.permonth / 30 + args.peryear / 360)
    print(kaef * choice[args.getby])


if __name__ == '__main__':
    main()
