import sys
digits = '1234567890'
classes = {}
for i in sys.stdin:
    i = i.split()
    if len(i) == 0:
        continue
    if i[-1][0] in digits:
        if int(i[-1]) not in classes.keys():
            classes[int(i[-1])] = []
        if ' '.join(i[0:-1]) in classes[int(i[-1])]:
            continue
        classes[int(i[-1])] += [' '.join(i[0:-1])]
for i in sorted(classes.keys()):
    print('{}: {}'.format(i, ', '.join(classes[i])))

