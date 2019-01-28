import sys

count, sort, num = False, False, False

for i in sys.argv:
    if i == '--count':
        count = True
    elif i == '--sort':
        sort = True
    elif i == '--num':
        num = True
    else:
        try:
            with open(i) as fl:
                text = fl.read().split('\n')
        except FileNotFoundError:
            print('ERROR')
            exit()
if sort:
    text = sorted(text)

for cnt, i in enumerate(text):
    if num:
        print(cnt, i)
    else:
        print(i)

if count:
    print('rows count: {}'.format(len(text)))
