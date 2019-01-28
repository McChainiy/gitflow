from yandex_testing_lesson import is_prime

tests = [(3, True), (11, True), (20, False), (100000000, False), (123, False), (117, False),
         (17, True), (25, False)]

for i in tests:
    if is_prime(i[0]) != i[1]:
        print('NO')
        break
else:
    print('YES')