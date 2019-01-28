import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sort', action='store_true')
    parser.add_argument('values', nargs='*')
    args = parser.parse_args()
    lst = {}
    for i in args.values:
        i = i.split('=')
        lst[i[0]] = i[1]
    if args.sort:
        srt = sorted(lst)
    else:
        srt = list(lst)

    for i in srt:
        print('Key: {}\tValue: {}'.format(i, lst[i]))


if __name__ == '__main__':
    main()