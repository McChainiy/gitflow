orig = input()
pal = input()

for i in range(len(orig)):
    if pal == orig:
        print(i)
        break
    pal = pal[1:] + pal[0]
else:
    print('-1')
