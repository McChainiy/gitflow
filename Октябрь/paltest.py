from yandex_testing_lesson import is_palindrome

tests = [('1', True), ('', True), ('23', False), ('2222', True)]

for i in tests:
    if not is_palindrome(i[0]) == i[1]:
        print('NO')
        break
else:
    print('YES')