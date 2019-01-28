letters = 'qwertyuiopasdfghjklzxcvbnm_'
workers = {}
for i in range(int(input())):
    adress = []
    for x in input().split('@')[0]:
        if x in letters:
            adress.append(x)
    adress = ''.join(adress)
    workers[adress] = workers.get(adress, 0) + 1
mail_adresses = []
for i in range(int(input())):
    name = input()
    mail_adresses.append('{}{}@untitled.py'.format(name, workers.get(name, '')))
    workers[name] = workers.get(name, 0) + 1
print(*mail_adresses, sep='\n')