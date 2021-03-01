def mul_12(x):
    twice = x + x  # 2*x
    fourth = twice + twice  # 4*x
    eighth = fourth + fourth  # 8*x
    return eighth + fourth


def mul_16(x):
    twice = x + x  # 2*x
    fourth = twice + twice  # 4*x
    eighth = fourth + fourth  # 8*x
    return eighth + eighth


def mul_15(x):
    twice = x + x  # 2*x
    fourth = twice + twice  # 4*x
    eighth = fourth + fourth  # 8*x
    return eighth - (0 - eighth) - x


def mul_29(x):
    twice = x + x  # 2*x
    fourth = twice + twice  # 4*x
    eighth = fourth + fourth  # 8*x
    sixteenth = eighth + eighth
    return sixteenth + sixteenth - (twice + x)


if __name__ == "__main__":
    print(mul_12(12))
    print(mul_16(5))
    print(mul_15(15))
    print(mul_29(10))
