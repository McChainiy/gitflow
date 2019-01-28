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


class BreakBye(PasswordError):
    pass


eng = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']

while True:
    try:
        parol = input()
        if parol == 'Ctrl+Break':
            raise KeyboardInterrupt
        if len(parol) <= 8:
            raise LengthError
        if (parol.isupper() or parol.islower()) or parol.isdigit():
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
        print('LengthError')
    except LetterError:
        print('LetterError')
    except DigitError:
        print('DigitError')
    except SequenceError:
        print('SequenceError')
    except KeyboardInterrupt:
        print('Bye-Bye')
        break
    else:
        print('ok')
        break
