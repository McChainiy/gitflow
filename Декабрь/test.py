OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
             '^': (3, lambda x, y: x ** y)}


def parse(line, x):
    num = ''
    skip = False
    for i in line:
        if i == 'x':
            yield float(x)
            skip = True
            continue
        if not num and i == '-' and not skip:
            num += i
            continue
        skip = False
        if i in '1234567890.':
            num += i
        elif num:
            yield float(num)
            num = ''
        if i in OPERATORS or i in '()':
            yield i
    if num:
        yield float(num)


def sort(parsed):
    tmp = []
    for i in parsed:
        if i in OPERATORS:
            while tmp and tmp[-1] != '(' and OPERATORS[i][0] <= OPERATORS[tmp[-1]][0]:
                yield tmp.pop()
            tmp.append(i)
        elif i == ')':
            while tmp:
                x = tmp.pop()
                if x == '(':
                    break
                yield x
        elif i == '(':
            tmp.append(i)
        else:
            yield i
    while tmp:
        yield tmp.pop()


def calc(sort):
    tmp = []
    print(sort, 'kek')
    for i in sort:
        print(i)
        if i in OPERATORS:
            y = tmp.pop()
            x = tmp.pop()
            tmp.append(OPERATORS[i][1](x, y))
        else:
            tmp.append(i)
    return tmp[0]


inp = input('Calculate: ')
print('Equall: ', calc(sort(parse(inp, 3))))