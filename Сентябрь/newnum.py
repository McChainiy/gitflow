class WrongLength(Exception):
    def __str__(self):
        return 'WrongLength'


class Minuses(Exception):
    def __str__(self):
        return 'TooMuchMinuses'


class BracketsError(Exception):
    def __str__(self):
        return 'BracketsError'


codes = [*list(range(910, 920)), *list(range(980, 990)), *list(range(920, 940)),
         *list(range(960, 970)), *list(range(902, 907))]

try:
    number = list(''.join(input().split()))
    if not((number[0] == '+' and number[1] == '7') or number[0] == '8'):
        raise Minuses
    if '--' in ''.join(number) or number[0] == '-' or number[-1] == '-':
        raise Minuses
    opened = False
    closed = False
    for i in range(len(number)):
        if number[i] == '(' and (opened or closed):
            raise BracketsError
        elif number[i] == '(':
            opened = True
            number[i] = ''
        elif number[i] == ')':
            if not opened or closed:
                raise BracketsError
            else:
                closed = True
                number[i] = ''
        elif number[i] == '-':
            number[i] = ''
    if opened and not closed:
        raise BracketsError
    per = 0
    if number[0] == '+':
        per = 1
    if ''.join(number[per:]).isdigit():
        number = ''.join(number)[per + 1:]
        if len(number) != 10:
            raise WrongLength
        if int(number[:3]) not in codes:
            raise ArithmeticError
        print('+7' + number)
    else:
        raise TypeError
except WrongLength:
    print('неверное количество цифр')
except Minuses:
    print('неверный формат')
except BracketsError:
    print('неверный формат')
except TypeError:
    print('неверный формат')
except ArithmeticError:
    print('не определяется оператор сотовой связи')