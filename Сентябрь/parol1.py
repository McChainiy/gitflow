class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


eng = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
parol = input()

try:
    if len(parol) <= 8:
        raise LengthError
    if (parol.isupper() and parol.islower()) or parol.isdigit():
        raise LetterError
    for i in parol:
        if i.isdigit():
            break
    else:
        raise DigitError
    for i in range(len(parol) - 2):
        combin = parol[i:i + 3]
        for x in eng:
            if combin.lower() in x:
                raise SequenceError
except LengthError:
    print('error')
except LetterError:
    print('error')
except DigitError:
    print('error')
except SequenceError:
    print('error')
else:
    print('ok')