rules = {'пират': ['камень', 'ножницы'], 'ножницы': ['бумага', 'ром'], 'бумага': ['пират', 'камень'],
         'камень': ['ром', 'ножницы'], 'ром': ['пират', 'бумага']}
first = input()
second = input()
if first in rules[second]:
    print('второй')
elif second in rules[first]:
    print('первый')
else:
    print('ничья')