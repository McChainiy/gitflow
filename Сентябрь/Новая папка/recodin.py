import sys


def translate(alpha):
    try:
        if alpha.islower():
            return dic[alpha]
        else:
            return dic[alpha.lower()].title()
    except KeyError:
        return alpha

f = open('cyrillic.txt', 'rt')
trans = f.read().replace('\n', '').replace('"', '').split(',')
f.close()
dic = {}
for i in trans:
    i = i.split(':')
    dic[i[0].lstrip()] = i[1].lstrip()
slated = []
for i in sys.stdin:
    slated.append(''.join(list(map(translate, i))).replace('\n', ''))
f = open('transliteration.txt', 'w')
for i in slated:
    print(i, file=f)
f.close()