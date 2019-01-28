import json
from sys import stdin


with open('scoring.json', 'r', encoding='utf-8') as fh:
    data = json.load(fh)['scoring']

curgroup = 0
scores = 0

for count, verd in enumerate(stdin, 1):
    verd = ''.join(verd.split())
    if count not in (data[curgroup]['required_tests']):
        curgroup += 1
    if verd == 'ok':
        scores += data[curgroup]['points'] // len(data[curgroup]['required_tests'])


print(scores)

