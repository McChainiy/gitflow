import copy
import random


def pprint(field):
    print()
    for i in field:
        for x in i:
            print('{}'.format(x), end='')
        print(end='\n')
    print()


def count_neighbors(field, i, j):
    neighbors = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:

            if not (0 <= i + x < len(field) and 0 <= j + y < len(field)):
                continue
            if x == 0 and y == 0:
                continue
            if field[i + x][j + y] == '*':
                neighbors += 1
    return neighbors


def turn(field):
    copy_field = copy.deepcopy(field)
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 'x':
                neighbors = count_neighbors(field, i, j)
                if neighbors == 3:
                    copy_field[i][j] = '*'
            elif field[i][j] == '*':
                neighbors = count_neighbors(field, i, j)
                if not(neighbors in [2, 3]):
                    copy_field[i][j] = 'x'
    return copy_field


size = int(input())
field = [list(input()) for i in range(size)]


was = []
cnt = 1
for i in range(12):
    field = turn(field)
    pprint(field)
    if field in was:
        print('Yes')
        print(cnt)
        break
    if field == [['x' for i in range(len(field))] for x in range(len(field))]:
        print('No')
        print(cnt)
        break
    was.append(field)

    cnt += 1
