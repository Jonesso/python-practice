# Вариант 17
import math


def f12(x):
    if x < 98:
        return math.log(x + math.cos(x)) + 3 * (x ** 8) + 99
    elif 98 <= x < 182:
        return x ** 2 / 2 + 70 * x
    elif x >= 182:
        return 57 * x ** 7 + x ** 6


# if __name__ == '__main__':
#     print("{:.2e}".format(f12(143)))
#     print("{:.2e}".format(f12(30)))
