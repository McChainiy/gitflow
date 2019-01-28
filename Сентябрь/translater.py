DIC = {'й': 'j', 'ц': 'c', 'у': 'u', 'к': 'k', 'е': 'e', 'н': 'n', 'г': 'g', 'ш': 'sh', 'щ': 'shh',
       'з': 'z', 'х': 'h', 'ъ': '#', 'ф': 'f', 'ы': 'y', 'в': 'v', 'а': 'a', 'п': 'p', 'р': 'r',
       'о': 'o', 'л': 'l', 'д': 'd', 'ж': 'zh', 'э': 'je', 'я': 'ya', 'ч': 'ch', 'с': 's', 'м': 'm',
       'и': 'i', 'т': 't', 'ь': "'", 'б': 'b', 'ю': 'ju', 'ё': 'jo'}


def translate(alpha):
    try:
        if alpha.islower():
            return DIC[alpha]
        else:
            return DIC[alpha.lower()].title()
    except KeyError:
        return alpha


data = []

with open('cyrillic.txt', 'r') as inp:
    for i in inp.read():
        data.append(translate(i))
with open('transliteration.txt', 'w') as outp:
    outp.write(''.join(data))
