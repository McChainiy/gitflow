import csv


def check(arr, kls):
    checking = [int(i) for i in arr[2].split('-')[2:4]]
    return checking == kls


klass = [int(i) for i in input().split()]

with open('rez.csv', 'r', newline='') as csvfile:
    reader = list(filter(lambda x: check(x, klass), list(csv.reader(csvfile,
                                                                    delimiter=',', quotechar='"'))))


reader = sorted(reader, key=lambda x: (int(x[-1]), (x[1].split()[3])), reverse=True)

with open('output.txt', 'w') as outp:
    for i in reader:
        outp.write('{} {}\n'.format(i[1].split()[3], i[-1]))
