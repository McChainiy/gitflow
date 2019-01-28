def strip_punctuation_ru(string):
    znaks = ''.join(['(),.!;":?', "'"])
    en_str = []
    for count, i in enumerate(list(string), 1):
        if i in znaks:
            en_str.append(' ')
        elif i == '-':
            if len(string) == count or list(string)[count] != ' ':
                en_str.append(i)
        else:
            en_str.append(i)
    return ' '.join(''.join(en_str).split())
