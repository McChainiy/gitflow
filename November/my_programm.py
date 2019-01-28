import sys
import argparse


def print_error(message):
    print('ERROR: {}!!'.format(message))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('msg', nargs=1)
    args = parser.parse_args()
    print('Welcome to my program')
    print_error(args.msg[0])


if __name__ == '__main__':
    main()
