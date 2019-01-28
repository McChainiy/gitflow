import sys


def check(mainw, secw):
    mainwcopy = list(mainw)
    for i in secw:
        if i not in mainwcopy:
            return False
        mainwcopy.remove(i)
    return True


mainword = input()
correct_words = []
for i in sys.stdin:
    thatword = i.rstrip('\n')
    if check(mainword, thatword):
        correct_words.append(thatword)
print(len(correct_words), *correct_words, sep='\n')

