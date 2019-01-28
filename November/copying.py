import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--upper', action='store_true', default=False)
    parser.add_argument('--lines', default=-1, type=int)
    parser.add_argument('files', nargs=2)
    args = parser.parse_args()
    with open(args.files[0]) as src_f:
        src = src_f.readlines()
        lent = len(src)
        args.lines = args.lines if 0 <= args.lines <= lent else lent
        out = []
        cnt = 0
        for i in src:
            if cnt == args.lines:
                break
            cnt += 1
            if args.upper:
                i = i.upper()
            out.append(i)
    with open(args.files[1], 'w') as dst:
        dst.write(''.join(out))


if __name__ == '__main__':
    main()