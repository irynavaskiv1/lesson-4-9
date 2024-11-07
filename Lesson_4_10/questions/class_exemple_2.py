"""
Рівні доступу до атрибутів класу:

Private. Приватні члени класу недоступні ззовні – з ними можна працювати лише усередині класу.

Public. Публічні методи навпаки - відкриті до роботи зовні і, зазвичай, оголошуються публічними відразу за замовчуванням.

Protected. Доступ до захищених ресурсів класу можливий лише всередині цього класу
і також усередині успадкованих від нього класів (іншими словами, усередині класів-нащадків).
Більше ніхто доступу до них не має.

"""


class Base:
    # Опис public method
    def fun(self):
        print("Публічний метод")

    # Опис protected method
    def _fun(self):
        print("Захищений метод")

    # Опис private method
    def __fun(self):
        print("Приватний метод")


# Створення нащадка
class Derived(Base):
    def __init__(self):
        # Виклик конструктора Base class
        Base.__init__(self)

    def call_public(self):
        # Виклик public method з base class
        print("\n В середині нащадка - публічний метод:")
        self.fun()

    def call_protected(self):
        # Виклик public method з base class
        print("\n В середині нащадка - захищений метод")
        self._fun()

    def call_private(self):
        # Виклик private method of base class
        print("\n В середині нащадка - приватний метод")
        self.__fun()


if __name__ == "__main__":
    obj1 = Base()
    obj1.fun()
    obj1._fun()
    # obj1.__fun()

    obj2 = Derived()
    obj2.call_public()
    obj2.call_protected()
    # obj2.call_private()
