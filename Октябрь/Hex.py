from sys import stdin


def convert(sym):
    tobe = str(hex(ord(sym)))[2:]
    return tobe if len(tobe) == 2 else '0' + tobe


def tohex(num):
    hexed = hex(num)[2:]
    return ''.join(('0' * (-len(hexed) + 5), hexed, '0'))


def check(sym):
    if sym.isprintable():
        return sym
    else:
        return '.'


text = [[]]

with open('data.txt', 'r') as data:
    f = data.readlines()
for i in f:
    for x in list(i):
        if len(text[-1]) != 16:
            text[-1].append(x)
        else:
            text.append([x])
print('          00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f  ')
print()
for i in range(len(text)):
    print('{}    {}{}   {}'.format(tohex(i), ' '.join(list(map(convert, text[i]))),
                                   (16 - len(text[i])) * '   ', ''.join(list(map(check, text[i])))))
