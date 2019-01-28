def reverse():
    f = open('input.dat', 'rb')
    dataf = f.read()
    print()
    f.close()
    f = open('output.dat', 'wb')
    dataf = str(dataf[::-1].decode())
    f.write(dataf.encode())
    f.close()


reverse()