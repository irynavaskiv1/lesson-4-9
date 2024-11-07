"""
Приклад використання технології "замикання" closures
для раціоналізації структури функціональної побудови коду
Сегмент виклика та запису результатів у файл - реалізовано за принципами замикання

"""


def calculator(func):
    def calculator_func(x, y, filename, text):
        func(x, y)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Операція: {text}, результат = {func(x, y)}\n\n")
            file.close()
            print("Операція:", text, "результат =", func(x, y))
        return

    return calculator_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x // y


if __name__ == "__main__":
    add_with_calculator = calculator(add)
    sub_with_calculator = calculator(sub)
    mult_with_calculator = calculator(mult)
    div_with_calculator = calculator(div)

    filename = "D:/Projects Python/Sigma_Python_Intensive/Lesson_4_10/calculator/add_with_calculator.txt"
    add_with_calculator(4, 6, filename, "add_with_calculator")

    filename = "D:/Projects Python/Sigma_Python_Intensive/Lesson_4_10/calculator/sub_with_calculator.txt"
    sub_with_calculator(8, 3, filename, "sub_with_calculator")

    filename = "D:/Projects Python/Sigma_Python_Intensive/Lesson_4_10/calculator/mult_with_calculator.txt"
    mult_with_calculator(2, 2, filename, " mult_with_calculator")

    filename = "D:/Projects Python/Sigma_Python_Intensive/Lesson_4_10/calculator/div_with_calculator.txt"
    div_with_calculator(10, 3, filename, "div_with_calculator")
