import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('integ', nargs='*')
    args = parser.parse_args()

    lent = len(args.integ)

    if lent == 0:
        print('NO PARAMS')
    elif lent == 1:
        print('TOO FEW PARAMS')
    elif lent > 2:
        print('TOO MUCH PARAMS')
    else:
        try:
            sys.stdout.write(str(int(args.integ[0]) + int(args.integ[1])))
        except ValueError:
            print('ValueError')
        except TypeError:
            print('TypeError')


if __name__ == '__main__':
    main()