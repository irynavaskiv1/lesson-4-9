'''
Приклади ітерованих об'єктів

'''

# словник
dict_example = dict(name="John", age=36, country="Norway")
for item in dict_example:
    print('thisdict_example = ', item)
print(dict_example, '\n')


# список
list_example = ["apple", "banana", "cherry"]
for item in list_example:
    print('list_example = ', item)
print(list_example, '\n')

# множина
set_example = set({"apple", "banana", "cherry"})
for item in set_example:
    print('set_example = ', item)
print(set_example, '\n')

# кортеж
tuple_example = [("Ashley", 93), ("Brad", 95), ("Cassie", 84)]
for item in tuple_example:
    print('tuple_example = ', item)
print(tuple_example, '\n')


