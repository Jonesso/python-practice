# Вариант 17
import math


def f11(x):
    return math.sqrt(math.log(x + math.cos(x)) + 3 * (x ** 3)) - math.sqrt(
        (x / 89 + x ** 3) / (x ** 4 + 10 * (x ** 2))) + math.sqrt(
        (10 * x + (x ** 2) / 94 + 9) / (x ** 2 / 30 + 2 * (x ** 4)))


# if __name__ == '__main__':
#     print("{:.2e}".format(f11(63)))
#     print("{:.2e}".format(f11(39)))
