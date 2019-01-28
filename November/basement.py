import sys

sys.stdin.readline()

changes = [int(i) for i in  sys.stdin.readline().split()]

tobeprinted = []

for i in range(int(input())):
    request = [int(i) for i in  sys.stdin.readline().split()]
    pl, mn = 0, 0
    for x in changes[request[0]:request[1] + 1]:
        if x < 0:
            mn += abs(x)
        elif x > 0:
            pl += x
    tobeprinted.append('{} {}'.format(pl, mn))


print(*tobeprinted, sep='\n')
