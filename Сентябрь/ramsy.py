file = open('input.txt', 'r')
f = file.read()
file.close()
dic = {1: 0, -1: 0, 0: 0}
for i in f.split():
    if int(i) < 0:
        dic[-1] += 1
    elif int(i) == 0:
        dic[0] += 1
    else:
        dic[1] += 1
file = open('output.txt', 'w')
tobeprinted = []
for i in sorted(dic.items(), key=lambda x: -x[1]):
    if i[1] != 0:
        tobeprinted.append('{} {}'.format(i[0], i[1]))
print('{}\n{}'.format(sum(dic.values()), ' '.join(tobeprinted)), file=file)
