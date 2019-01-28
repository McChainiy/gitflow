from math import sqrt
n = int(input())

ranged = []

for i in range(1, n + 1):
    if n % i == 0:
        ranged.append(i)


for i in ranged:
    sq = n / i
    if sqrt(sq).is_integer():
        print(int(sq))
        break