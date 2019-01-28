import csv


def recurs(current, final, price=0):
    paths = []
    if current[-1] == final:
        return current + [price]
    try:
        for i in ways[current[-1]]:
            res = recurs(current + [i[0]], final, i[1] + price)
            if res:
                res.append('#')
                paths = paths + res
    except KeyError:
        return False
    return paths


ways = {}

with open('input.csv', 'r', newline='') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';', quotechar='"'))
finish = reader[-1][:2]
for i in reader[:-1]:
    ways[i[0]] = ways.get(i[0], []) + [(i[1], int(i[2]))]
results = [[]]
for i in recurs([finish[0]], finish[1]):
    if i != '#':
        results[-1].append(i)
    else:
        results.append([])
while [] in results:
    results.remove([])
print(*min(results, key=lambda x: x[-1])[:-1])