'''
Мій власний ітератор - Iterator
'''


import sys


class MyRangeIterator:

    def __init__(self, start:int, end:int, step:int = 1):       # задати параметри повторень - ітерацій ітератора в методі - конструкторі
        self.value = start
        self.end = end
        self.step = step

    def __iter__(self):                                         # описати метод  ітератора - "декларація" ітератора
        # тут може бути унікальна логіка (зустрічається рідко) або пуста структура
        return self

    def __next__(self):                                         # описати метод повторень - ітерацій ітератора - "новий елемент"
        if self.value >= self.end:
            raise StopIteration                                 # контроль зупинки виконання повторень, інакше - нескінченість повторень
        current = self.value
        self.value += self.step
        return current


if __name__ == '__main__':
    my_iter = MyRangeIterator(1, 11)

    for i in my_iter:
        print(i)

    my_iter2 = MyRangeIterator(1, 10, 3)

    print(sys.getsizeof(my_iter2))                             # створений ітератор
    print(sys.getsizeof(range(1, 10, 3)))                      # вбудований ітератор - сутність, що ітерується

    # print(next(my_iter2))
    # print(next(my_iter2))
    # print(next(my_iter2))
