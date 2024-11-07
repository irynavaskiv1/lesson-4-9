"""
Рівні доступу до атрибутів класу:

Private. Приватні члени класу недоступні ззовні – з ними можна працювати лише усередині класу.

Public. Публічні методи навпаки - відкриті до роботи зовні і, зазвичай, оголошуються публічними відразу за замовчуванням.

Protected. Доступ до захищених ресурсів класу можливий лише всередині цього класу
і також усередині успадкованих від нього класів (іншими словами, усередині класів-нащадків).
Більше ніхто доступу до них не має.

"""


class Phone_public:
    def __init__(self, color):
        # публічне поле color (public)
        self.color = color


class Phone_protected:
    def __init__(self, color):
        # Захищене поле _color (protected)
        self._color = color


class Phone_privat:
    def __init__(self, color):
        # приватне поле __color (private)
        self.__color = color
        print(self.__color)


if __name__ == "__main__":
    obj1 = Phone_public("Публічне поле: white")
    print(obj1.color)

    obj2 = Phone_protected("Захищене поле: yellow")
    print(obj2._color)

    obj3 = Phone_privat("Приватне поле: red")
    # print(obj3.__color)
