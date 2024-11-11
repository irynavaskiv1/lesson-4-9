'''
Ітератор - Iterator та його особливості:

'''


from pprint import pprint
import sys

# Створення демонстраційного списку
nums = [1, 2, 3]
# nums = [1, 2, 3, 5, 7, 8, 10, 11, 1, 2, 3, 5, 7, 8, 10, 11, 1, 2, 3, 5, 7, 8, 10, 11, 1, 2, 3, 5, 7, 8, 10, 11]

if __name__ == '__main__':

    # Створення демонстраційного ітератора
    iter_str = iter('Hello')
    iter_set = iter({'Hello', 'Python'})

    print('Створено ітератор: ', iter_str)
    print('Створено ітератор: ', iter_set, '\n')

    # Доступні Dunder-методи ітератора
    # print('Доступні Dunder-методи ітератора: ')
    # pprint(dir(iter_str))

    # Створення ітератора відбувається шляхом його "перевикористання" - економія ресурсів пам'яті
    print("Створення ітератора відбувається шляхом його перевикористання - економія ресурсів пам'яті")
    print('nums =', nums)
    print('type(nums) =', type(nums))
    iterator = iter(nums)
    iterator2 = iter(iterator)
    print('Порівняння:', iterator is iterator2)
    print('Порівняння:', iterator, ' ', iterator2, '\n')

    # Структура ітератора забезпечує економію ресурсів пам'яті
    # print("Структура ітератора забезпечує економію ресурсів пам'яті")


    nums_iter = iter(nums)

    # print("Пам'ять nums, байт =", sys.getsizeof(nums))
    # print("Пам'ять nums_iter, байт =", sys.getsizeof(nums_iter))
    # print("Ітератор має лише посилання на обє'кт та звертається до конструкції, що ітерується після звернення до ітератора")
    # print(next(nums_iter))
    # print(next(nums_iter))
    # print(next(nums_iter))

    # print("Контроль проходження ітератора по компонентам - ітератор - одноразовий процес - інакше виключення StopIteration")
    # print([num for num in nums_iter])
    # print(list(nums_iter))
    # for num in nums_iter:
    #     print(num)
