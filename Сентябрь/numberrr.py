from sys import stdin


for i in stdin:
    try:
        number = ''.join(i.split())
        if number[0] == '+' and number[1] == '7':
            ots = 2
        elif number[0] == '8':
            ots = 1
        else:
            raise ValueError
        if '(' in number or ')' in number:
            if not(number[ots] == '(' and number[ots + 4] == ')'):
                raise ValueError
            elif number.count('(') > 1 or number.count(')') > 1:
                raise ValueError
        if '--' in number or number[0] == '-' or number[-1] == '-':
            raise ValueError
        for z in '-)(+':
            if z in number:
                number = number.replace(z, '')
        if len(number) != 11:
            raise ValueError
        if number.isdigit():
            print('YES')
        else:
            raise ValueError
    except ValueError:
        print('NO')
    except Exception:
        print('NO')
