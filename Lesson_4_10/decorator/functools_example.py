"""
Приклад використання декоратора - з модулем pprint  для форматування відображення даних
Особливість:
один декоратор @prettify() - з параметрами +, або -
використання конструкції  @wraps(func)
wraps() — це декоратор, який застосовується до функції обгортки декоратора.
https://www.geeksforgeeks.org/python-functools-wraps-function/

"""

from functools import wraps  # імпорт декоратора wraps()
import pprint


def prettify(indent=1, depth=None):
    def inner_function(func):
        @wraps(
            func
        )  # wraps() — це декоратор, який застосовується до функції обгортки декоратора.
        def wrapper(*args, **kwargs):
            return pprint.pformat(func(*args, **kwargs), indent=indent, depth=depth)

        return wrapper

    return inner_function


@prettify()
def get_data():
    """
    Повертає щось цікаве
    """
    return {i: {"a": "A", "b": "B", "c": "C", "d": "D"} for i in range(3)}


@prettify(indent=2, depth=2)
def get_nested_data_with_parameter(x):
    """
    Повертає щось набагато цікавіше - словничок dict з параметрами indent=2, depth=2
    """
    return {
        i: {"a": {"A": "a"}, "b": {"B": "b"}, "c": {"C": "c"}, "d": {"D": "d"}}
        for i in range(x)
    }


if __name__ == "__main__":
    # print(get_data())
    print(get_nested_data_with_parameter(5))
