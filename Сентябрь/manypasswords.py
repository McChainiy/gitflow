import time

data = open("top 10000 passwd.txt").read().split()
words = open("top-9999-words.txt").read().split()

start = time.time()


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


class WordError(PasswordError):
    pass


eng = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']


def check_password(parol, attempt=[0]):
    try:
        if attempt[-1] == 0:
            if len(parol) <= 8:
                raise LengthError
        if attempt[-1] < 2:
            lower, upper = False, False
            for i in parol:
                if i.islower():
                    lower = True
                if i.isupper():
                    upper = True
            if not (lower and upper):
                raise LetterError
        if attempt[-1] < 3:
            for i in words:
                if i in parol:
                    raise WordError
        if attempt[-1] < 4:
            for i in parol:
                if i.isdigit():
                    break
            else:
                raise DigitError
        if attempt[-1] < 5:
            for i in range(len(parol) - 2):
                combin = parol[i:i + 3]
                for x in eng:
                    if combin.lower() in x:
                        raise SequenceError
        return attempt
    except LengthError:
        return check_password(parol, attempt + [1])
    except LetterError:
        return check_password(parol, attempt + [2])
    except WordError:
        return check_password(parol, attempt + [3])
    except DigitError:
        return check_password(parol, attempt + [4])
    except SequenceError:
        return check_password(parol, attempt + [5])


mistakes = {'LengthError': 0, 'LetterError': 0, 'WordError': 0, 'DigitError': 0,
            'SequenceError': 0}

for i in data:
    checked = check_password(i)[1:]
    for x in checked:
        mistakes[list(mistakes.keys())[x - 1]] += 1
for i in sorted(mistakes.keys()):
    print('{} - {}'.format(i, (mistakes)[i]))
