"""
Приклад: навіщо wraps() !?
wraps() — це декоратор, який застосовується до функції обгортки декоратора.
https://www.geeksforgeeks.org/python-functools-wraps-function/
Це про доступність імен функції в огортанні декоратора - а відтак про виклик функції, передачу параметрів тощо

"""

from functools import wraps


def log_decorator(func):
    def wrapper():
        """
        конструкція  __name__  це магічний / dunder метод, що дає доступ до ім'я - функції hello_world()
        """

        print(f"Виклик функції {func.__name__}")
        func()

    return wrapper


@log_decorator
def hello_world():
    print("Hello, world!")


print("------- без wraps() ----------")
hello_world()  # посилання на ім'я функції до її виклику
print("Без wraps(): ", hello_world.__name__)  # посилання на ім'я функції що є wrapper
print(
    "Без wraps(): ", hello_world.__doc__
)  # посилання на документацію функції що є wrapper


# ----------------------------------------------------------------------------------------------------------


def log_decorator(func):
    """
    wraps() — це декоратор, який застосовується до функції обгортки декоратора.
    Він оновлює функцію оболонки, щоб вона виглядала як обернена функція,
    копіюючи такі атрибути, як __name__, __doc__ (рядок документа) тощо.
    """

    @wraps(func)
    def wrapper():
        print(f"Виклик функції: {func.__name__}")
        func()

    return wrapper


@log_decorator
def hello_world():
    """
    Приклад: навіщо wraps() !?
    """
    print("Hello, world!")


print("------- працює wraps() ----------")
hello_world()  # посилання на ім'я функції до її виклику
print(
    "Працює wraps(): ", hello_world.__name__
)  # посилання на ім'я функції що є hello_world()
print(
    "Працює wraps(): ", hello_world.__doc__
)  # посилання на документацію функції що є hello_world()
