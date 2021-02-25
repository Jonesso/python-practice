# Вариант 17
def f13(n):
    sum1 = 0
    sum2 = 0

    for i in range(1, n + 1):
        sum1 += 36 * i ** 6 - i ** 7
        sum2 += i ** 2 / 30 + 2 * i ** 4

    return sum1 / 66 + 94 * sum2


# if __name__ == '__main__':
#     print("{:.2e}".format(f13(91)))
#     print("{:.2e}".format(f13(43)))
