def tonormal(hour, minute):
    hour = [int(i) for i in str(hour)]
    minute = [int(i) for i in str(minute)]
    if len(hour) == 1:
        hour.insert(0, 0)
    if len(minute) == 1:
        minute.insert(0, 0)
    if sum(hour) != sum(minute):
        print('{}{}:{}{}'.format(hour[0], hour[1], minute[0], minute[1]))


hours = [int(i) for i in input().split()]
minutes = [int(i) for i in input().split()]
for i in sorted(hours):
    for x in sorted(minutes):
        tonormal(i, x)