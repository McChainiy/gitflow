import random
f = open('lines.txt', 'rt')
data = f.readlines()
f.close()
print(data[random.randint(1, len(data)) - 1][:-1]) if data != [] else None
