'''
Вбудовані ітератори - Iterator

'''


import os
import sys
from pprint import pprint as print

nums = [1, 2, 3]


if __name__ == '__main__':

    print('Демонстрація можливостей динамічної типізації')
    print(enumerate(nums))                  # створює кортеж (tuple): індекс:значення - ітератор
    print(dict(enumerate(nums)))            # створює словник (dict)
    print(list(enumerate(nums)))            # створює список (list)


    print('Демонстрація можливостей функція zip')
    print(zip(nums, nums))
    print(list(zip(nums, nums)))           # функція zip створює пару з першого та другого елементу конструкції, що ітерується
    print(dict(zip("ABC", nums)))


    print('Демонстрація можливостей функція reversed')
    print(reversed(nums))
    print(list(reversed(nums)))             # зміна послідовності елементів конструкції, що ітерується


    print('Демонстрація можливостей роботи із файлами')
    print(f := open(os.path.join("demo","demo.txt")))
    # for item in f:
    #     print(item)

    # print(list(f))



    print('Коректна конструкція роботи із файлами')
    try:
        while True:
            print(next(f))
    except StopIteration:
        print("Stopped")
    
    print(sys.getsizeof(f.readlines()))
    print(sys.getsizeof(f.__iter__))

    f.close()
