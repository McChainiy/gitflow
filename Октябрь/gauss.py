def recurs(now, inst):
    global count, found
    if found:
        return
    if sum(now) == 0:
        print(count)
        found = True
        return now
    if abs(sum(now)) > ((len(now) * (len(now) + 1)) / 2):
        return
    count += 1
    for i in range(inst, len(now)):
        now[i] = -now[i]
        a = recurs(now, inst + 1)
        if a:
            return a

for toran in list(range(100))[1:]:
    found = False
    count = 0

    if ((toran * (toran + 1)) / 2) % 2 != 0:
        print('IMPOSSIBLE', toran)
    else:
        a = recurs(list(range(toran + 1))[1:], 0)
        for i in a:
            if i < 0:
                print('-', end='')
            else:
                print('+', end='')
        print(' ', toran)
    print()




