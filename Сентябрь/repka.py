chars = [False] + [i for i in input().split(' -> ')] + [False]
forgetters = [chars.index(input()) for i in range(int(input()))]
for i in forgetters:
    was = False
    for x in range(i - 1, i + 2):
        zet = chars[x]
        if zet:
            if was:
                print(' -> ', end='')
            print(zet, end='')
            was = True
    print(end='\n')