"""
Приклад використання технології декоратора - decorator як продовження технології "замикання" - closures
Зверніть увагу на:
- wrapper(x, y): # обгортка декоратора https://www.geeksforgeeks.org/function-wrappers-in-python/
- декораторів ДЕКІЛЬКА !!!
- узгодження аргументів функцій - декоратора та ієрархію виклику декоратора.

"""


def calculator(func):
    def wrapper(
        x, y
    ):  # обгортка декоратора https://www.geeksforgeeks.org/function-wrappers-in-python/
        # print('результат_calculator =', func(x, y))
        return func(x, y)

    return wrapper


def write_to_file(func):
    def wrapper(x, y, filename, text):
        # def wrapper(x, y):                         # демонстрація ієрархії декораторів
        # func(x, y)
        # print('результат =', func(x, y))

        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Операція: {text}, результат = {func(x, y)}\n\n")
            file.close()
            print("Операція:", text, "результат =", func(x, y))
        return

    return wrapper


@write_to_file  # декоратор верхнього рівня - ієрархія декораторів
@calculator
def add(x, y):
    return x + y


@write_to_file
@calculator
def sub(x, y):
    return x - y


@write_to_file
@calculator
def mult(x, y):
    return x * y


@write_to_file
@calculator
def div(x, y):
    return x // y


if __name__ == "__main__":
    filename = "D:/Projects Python/Sigma_Python_Intensive/Lesson_4_10/calculator/add_with_calculator.txt"
    add(4, 6, filename, "add")
    # add(4, 6)                     # демонстрація ієрархії декораторів

    filename = "D:/Projects Python/Sigma_Python_Intensive/Lesson_4_10/calculator/sub_with_calculator.txt"
    sub(8, 3, filename, "sub")

    filename = "D:/Projects Python/Sigma_Python_Intensive/Lesson_4_10/calculator/mult_with_calculator.txt"
    mult(2, 2, filename, " mult")

    filename = "D:/Projects Python/Sigma_Python_Intensive/Lesson_4_10/calculator/div_with_calculator.txt"
    div(10, 3, filename, "div")
