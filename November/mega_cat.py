import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', action='store_true')
    parser.add_argument('--sort', action='store_true')
    parser.add_argument('--num', action='store_true')
    parser.add_argument('text', nargs=1)
    args = parser.parse_args()
    try:
        with open(args.text[0]) as fl:
            text = fl.read().split('\n')
    except FileNotFoundError:
        print('ERROR')
        return
    if args.sort:
        text = sorted(text)

    for cnt, i in enumerate(text):
        if args.num:
            print(cnt, i)
        else:
            print(i)

    if args.count:
        print('rows count: {}'.format(len(text)))


if __name__ == '__main__':
    main()
