"""
Замикання closures Python — це внутрішні функції, вкладені в зовнішню функцію.
Замикання можуть отримати доступ до змінних, присутніх у зовнішній області видимості функції.
Можливо отримати доступ до цих змінних навіть після того, як зовнішня функція завершить своє виконання.

Замикання застосовується для динамічного виклику функцій.
"""


def printer(msg: str):
    message = msg

    print(message)

    def inner_func():
        # print(message)       # змінна message - замкнулась у функції inner_func
        print("Inner " + message)  # змінна message - замкнулась у функції inner_func

    print(message)

    return inner_func  # функція printer повертає функцію inner_func - ОСОБЛИВІСТЬ замикання !!!


if __name__ == "__main__":
    hello_func = printer("Hello")  # змінна є функцією
    hello_func()  # викликаємо функцію за ім'ям змінної - ОСОБЛИВА поведінка внутрішньої функції на замиканні !!!

    # hello_func("World")

    # hello_func = printer("Hello")
    # World_func = printer("World")
    # hello_func()
    # World_func()
