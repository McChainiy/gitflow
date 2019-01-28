import sys
questions = set()
belissimo = set()
just = set()
sings = '.!?'
cur_snt = []
for i in sys.stdin:
    i = i.split()
    for x in i:
        cur_snt.append(x)
        for sign in sings:
            if sign in x:
                for j in cur_snt:
                    if sign == '.':
                        if sign in j:
                            just.add(j[:-1].lower())
                        else:
                            just.add(j.lower())
                    elif sign == '!':
                        if sign in j:
                            belissimo.add(j[:-1].lower())
                        else:
                            belissimo.add(j.lower())
                    elif sign == '?':
                        if sign in j:
                            questions.add(j[:-1].lower())
                        else:
                            questions.add(j.lower())
                cur_snt = []
cor_words = []
for i in just:
    if i not in belissimo and i in questions:
        cor_words.append(i)
print(*sorted(cor_words), sep=' ')