codes = [*list(range(910, 920)), *list(range(980, 990)), *list(range(920, 940)),
         *list(range(960, 970)), *list(range(902, 907))]

country_codes = ['+359', '+55', '+1', '+7']


class WrongLength(Exception):
    pass


class Minuses(Exception):
    pass


class BracketsError(Exception):
    pass


class CountryCode(Exception):
    pass


russia = True

try:
    number = list(''.join(input().split()))
    if not((number[0] == '+' and number[1] == '7') or number[0] == '8'):
        try:
            if number[0:4] == list(country_codes[0]):
                russia = False
            elif number[0:3] == list(country_codes[1]):
                russia = False
            elif number[0:2] == list(country_codes[2]):
                russia = False
            else:
                raise CountryCode
        except IndexError:
            raise WrongLength
        except CountryCode:
            raise CountryCode
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
            if russia:
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
except CountryCode:
    print('не определяется код страны')
