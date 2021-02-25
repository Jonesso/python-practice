# Вариант 17
import math


def f14(n):
    if n == 0:
        return 7
    else:
        return math.cos(f14(n - 1)) + f14(n - 1) / 65


# if __name__ == '__main__':
#     print("{:.2e}".format(f14(16)))
#     print("{:.2e}".format(f14(13)))
