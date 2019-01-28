import math


def conv(word):
    return [int(i) for i in word.split()]


R, u, v = conv(input())
towers = []
for i in range(int(input())):
    towers.append(conv(input()))
my_coords = conv(input())

summ = 0

for i in towers:
    s = math.sqrt((-my_coords[0] + i[0]) ** 2 + (-my_coords[1] + i[1]) ** 2)
    if s <= (R / 2):
        summ += u
    elif R / 2 < s <= R:
        summ += v

print(summ)
