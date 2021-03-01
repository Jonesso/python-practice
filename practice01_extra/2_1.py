"""
Задача 1.
Некто попытался реализовать "наивную" функцию умножения с помощью сложения.
К сожалению, в коде много ошибок. Сможете ли вы их исправить?
Добавьте к naive_mul автоматическое тестирование для проверки обоих
аргументов в диапазоне от 0 до 100. Сравнивайте с встроенным умножением,
используя конструкцию assert.
"""


def naive_mul(x, y):
    res = 0
    for _ in range(y):
        res += x
    return res


def test_func():
    for x in range(101):
        for y in range(101):
            assert naive_mul(x, y) == x * y
    print("All tests passed")


if __name__ == "__main__":
    test_func()
