'''
Приклад генератора-функції (генераторна функція)
'''


def my_generator(start, end, step=1):  # генератор реалізовано на принципах range() - Iterator

    '''

    :param start: int
    :param end: int
    :param step: int
    :return: Generator (from typing import Generator)

    Інструкція yield призупиняє виконання функції та надсилає значення як результат її виклику,
    але зберігає поточний стан, щоб функція могла продовжити роботу з того місця, де вона зупинилася.
    Коли функція відновлює роботу, вона продовжує виконання одразу після останнього запуску yield.
    Це дозволяє його коду виробляти ряд значень з часом, а не обчислювати їх одразу та надсилати назад як список.
    https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/

    '''

    #----------------------------- це ГЕНЕРАТОР ------------------------------------

    current = start
    while current <= end:
        yield current           # якщо генератор є фабрика, то yield повертає продукт фабріки
        yield current ** 2
        current += step

    # ------------------------- це НЕ генератор ------------------------------------
    # current = start
    # while current <= end:
    #     return current
    #     current += step



my_gen = my_generator(1, 10)

if __name__ == '__main__':
    print(my_gen)
    print(type(my_gen))
    for x in my_gen:
        print(x)