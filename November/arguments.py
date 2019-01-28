import sys

sort = False
lst = {}

for i in sys.argv:
    if i == '--sort':
        sort = True
    elif '=' in i:
        lst[i.split('=')[0]] = i.split('=')[1]

if sort:
    srt = sorted(lst)
else:
    srt = list(lst)

for i in srt:
    print('Key: {} Value: {}'.format(i, lst[i]))
