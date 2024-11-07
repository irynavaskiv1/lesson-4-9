"""

Приклад використання декоратора - з модулем pprint  для форматування відображення даних
Особливість в аргументах *args, **kwargs - порядку інформаційної взаємодії в декораторах.
*argsі **kwargs дозволяють передавати функції кілька аргументів або ключових аргументів
*args - аргументи не повязані із ключовими словами;
**kwargs - аргументи ключових слів.
https://www.geeksforgeeks.org/args-kwargs-python/
https://realpython.com/python-kwargs-and-args/

"""

import pprint as pp


def pretty_with_params(indent=1):  # функція приймає параметр налаштування
    def inner_func(func):  # функція приймає функцію - технології замикання
        def wrapper(*args, **kwargs):
            return pp.pformat(func(*args, **kwargs), indent=indent)

        return wrapper

    return inner_func


def pretty_without_params(func):  # функція приймає функцію - технології замикання
    # def inner_func(func):

    def wrapper(*args, **kwargs):
        return pp.pformat(func(*args, **kwargs), indent=1)

    return wrapper

    # return inner_func


@pretty_with_params(indent=10)
# @pretty_without_params
def get_data():
    return [(i, {"a": "A", "b": "B", "c": "C", "d": "D"}) for i in range(3)]


@pretty_with_params(indent=1)
@pretty_without_params
def get_data_with_parameter(x):
    return [(i, {"a": "A", "b": "B", "c": "C", "d": "D"}) for i in range(x)]


if __name__ == "__main__":
    print(get_data())
    # print(get_data_with_parameter(5))
