import sys
import argparse


def count_lines(path):
    try:
        with open(path) as file:
            lent = sum(1 for i in file)
    except Exception:
        return '0'
    else:
        return str(lent)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    args = parser.parse_args()
    print(count_lines(args.file))


if __name__ == '__main__':
    main()