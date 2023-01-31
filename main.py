def decor(func):
    def wrap(*args):
        print("Среднее арифметическое чисел", str(args)[1:-1], "=", func(*args) / len(args))
    return wrap


@decor
def summ(*args):
    print("Сумма чисел", str(args)[1:-1], "=", sum(args))
    return sum(args)


summ(2, 3, 3, 4)


