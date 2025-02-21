
text = 'text'
text += ' new'
print(text)

simbol = '*'
simbol *= 25
print(simbol)
print('Copyrights')
print(simbol)

# Оператор принадлежности
text = 'I love Python'
print('love' in text)
print('Love' in text)


# Оператор идентичности

b = 2
print(id(b))
c = 2
print(id(c))

d = 257
print(id(d))
e = 257
print(id(e))
print(d is c)
print(d is not c)


my_list = [1, 2, 3, 7, None, 'text', False, 2.43, 'last']

print(my_list)
print(my_list[-3])
my_list[2] = 42
print(my_list)

# Создание пустого списка
my_list = []
# my_list = list()

"""Добавление элементов в список"""

my_list.append('text')
my_list.append(42)
my_list.append(155)
print(my_list)

print(len(my_list))  # Длина списка

print(my_list.index('text'))  # Индекс элемента

my_list.pop(0)  # Удаление элемента, он хранит в себе удаленные данные
poped = my_list.pop(0)  # Переменая которая хранит удаленый элемент
print(my_list)
print(poped)


# TODO Tuple (Кортеж)

my_tuple = (1, 2, 3, 7, None, 'text', 7, False, 2.43, 7, 'last')
print(my_tuple[1])
print(my_tuple.count(4))  # Подсчет кол-во элемента в list/tuple
print(my_tuple.index(None))

llist = [56]
print(type(llist))
ttuple = (56,)  # Создат пустой tuple
print(type(ttuple))
ttuple = (56)  # Создат переменую int
print(type(ttuple))


# TODO Set (множество)

my_set = {1, 2, 3, 7, None, 'text', 7, False, 2.43, 7, 'last'}
print(my_set)
my_set.add(42)
print(my_set)

# Преобразование list в set и обратно
# Удаление повторных значений в list

list_1 = list({1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'text', 'text'})   # Избавление от повторов в list
list_2 = list(set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 'text', 'text']))   # Преобразование в set и обратно в list
print(list_1)
print(list_2)

list_3 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 'text', 'text']
print(list_3)
list_3 = set(list_3)
print(list_3)
list_3 = list(list_3)
print(list_3)

# Создание пустого set возможно только так
my_set = set()


# TODO Dictionary (словарь)

my_dict = {'one': 'value', 'two': 'value2'}
print(my_dict['one'])
print(my_dict)
print(len(my_dict))
my_dict['one'] = 'myone'
print(my_dict)
my_dict['theree'] = 'value3'
print(my_dict)


#  Ключами могут быть только неизменяемые типы данных

my_dict['four'] = False
my_dict['five'] = [1, 5, 8]
my_dict['six'] = {1, 6, 9}
my_dict[2] = 'ключ int'
my_dict[False] = 'ключ bool'
my_dict[2.42] = 'ключ floot'
my_dict[(1, 2)] = 'ключ set'
my_dict[5] = {1: 2}   # Словарь может быть значением


print(my_dict)

print(my_dict.keys())    # Получить все ключи
print(my_dict.values())  # Получить все значения
print(my_dict.items())   # Получить весь словарь



