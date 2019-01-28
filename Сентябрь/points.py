osb = []
left, right, top, bottom = False, False, False, False
for i in range(int(input())):
    kek = tuple([int(z) for z in input().split()])
    if abs(kek[0]) > abs(kek[1]):
        osb.append(kek)
    if not left or kek[0] < left[0]:
        left = kek
    if not right or kek[0] > right[0]:
        right = kek
    if not top or kek[1] > top[1]:
        top = kek
    if not bottom or kek[1] < bottom[1]:
        bottom = kek

for i in osb:
    print(i)
print('left:', left)
print('right:', right)
print('top:', top)
print('bottom:', bottom)