"""
Приклад використання декораторів для класів.
https://www.geeksforgeeks.org/class-as-decorator-in-python/
Використано магічний / dunder методи:
__init__ - конструктор;
__call__ - метод дозволяє писати класи, де екземпляри поводяться як функції та можуть бути викликані як функція.
https://www.geeksforgeeks.org/__call__-in-python/

"""

from time import time


class benchmark:  # оцінювання швидкодії функціі
    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start_time = time()
        print(start_time)
        result = self.function(*args, **kwargs)
        end_time = time()
        print(end_time)
        # delta = float(end_time - start_time)
        # print(f"Executed in {format(delta, '.12g')} seconds")
        print(f"Executed in {end_time - start_time} seconds")
        return result


@benchmark
def get_power(n):
    print(n**100)


@benchmark
def factorial(n):
    result = 1
    for item in range(1, n + 1):
        result *= item
    return result


# get_power(10000)
print(factorial(1510))
# print(factorial(10))
