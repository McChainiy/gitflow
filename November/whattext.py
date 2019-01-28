dic = {}
azbuka = 'abcdefghijklmnopqrstuvwxyz '


def to_normal(string):
    return ''.join(list(filter(lambda x: x in azbuka, string[:-1].lower())))


with open('nti_text.txt') as file:
    for i in file.readlines():
        for x in to_normal(i).split():
            dic[x] = dic.get(x, 0) + 1

with open('solution.txt', 'w') as file:
    for i, x in sorted(dic.items(), key=lambda x: (-x[1], x[0]), reverse=False):
        file.write('{} {}\n'.format(i, x))
