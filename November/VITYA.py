a, b, c = [int(i) for i in input().split()]

if c >= b:
    print(0)
    exit()
cnt = 1
while True:
    if (a * cnt) % b == c:
        print(cnt)
        break
    if cnt == b + 1:
        print(0)
        break
    cnt += 1
