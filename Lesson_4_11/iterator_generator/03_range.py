'''
А що про range() - це ітератор - Iterator?
'''


new_range = range(1, 10)


if __name__ == '__main__':

    print(new_range)
    print(type(new_range))
    print(iter(new_range))

    # print(list(new_range))

    print(dir(new_range))
    # print(next(new_range))