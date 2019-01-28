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


eng = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ',
       'фывапролджэ', 'ячсмитьбю', '1234567890']
parol = input()

try:
    assert len(parol) > 8
    assert not((parol.isupper() and parol.islower()) or parol.isdigit())
    for i in parol:
        if i.isdigit():
            break
    else:
        raise Exception
    for i in range(len(parol) - 2):
        combin = parol[i:i + 3]
        for x in eng:
            if combin.lower() in x:
                raise Exception
except AssertionError:
    print('error1')
except Exception:
    print('error')
else:
    print('ok')