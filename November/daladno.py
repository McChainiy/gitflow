import sys

summ = 0
coef = 1
if len(sys.argv) == 1:
    print('NO PARAMS')
    exit()
try:
    for i in sys.argv[1:]:
        summ += int(i) * coef
        coef *= -1
except ValueError:
    print('ValueError')
else:
    print(summ)
