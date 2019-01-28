import sys


menulength = int(input())
menu = {}
for i in range(menulength):
    dish = input().split()
    name = []
    for i in dish:
        if i.isdigit():
            price = int(i)
        else:
            name.append(i)
    name = ' '.join(name)
    menu[name] = price
print(menu)
started = False

orders = []
for i in sys.stdin:
    i = ' '.join(i.split())
    print(i)
    if i == '.':
        print('suka')
        break
    if not started:
        if i == '------------------------':
            started = True
        continue
    if i == '':
        continue
    order = input().split()
    name = []
    for x in order:
        if x.isdigit():
            count = int(x)
        else:
            name.append(x)
    name = ' '.join(name)
    print(name, count)
    orders.append(menu[name] * count)

print(orders)