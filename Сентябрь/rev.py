def reverse():
    with open('input.dat', 'rb') as inp:
        data = inp.read()[::-1]
    with open('output.dat', 'wb') as outp:
        outp.write(data)
