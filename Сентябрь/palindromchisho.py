def palindrome():
    with open('input.dat', 'rb') as inp:
        data = inp.read()
        return data[::-1] == data
