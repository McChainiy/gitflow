from math import sqrt


def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    for divisor in range(2, int(sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True


if is_prime(input()):
    print('YES')
else:
    print('NO')