# TODO Распаковка

my_list = [1, 3]
my_tuple = (2, 6, 9)

# a = my_list[0]
# b = my_list[1]
# c = my_tuple[0]
# d = my_tuple[1]
# e = my_tuple[2]

a, b = my_list  # Передали каждое значение list в переменую
c, d, e = my_tuple  # Передали каждое значение tuple в переменую

# print(a, b, c, d, e)


# TODO Срез

lll = [1, 3, 5, 2, 5, 7, 1, 3]

print(lll)
print(lll[1:4])
print(lll[:4])
print(lll[3:])
print(lll[1::2])
print(lll[:])
print(lll[::-1])
print(lll[-2:-6:-1])

# TODO Методы строк

text = 'my long long string'
print(text[3])
print(len(text))
print(text.index('long'))
print('long' in text)
print(text.count('long'))
print(text.count('s'))
print(text.find('longq'))  # Вернет не ошибку, а -1\\
print(text[:7])
print(text.startswith('my'))

txt = 'This tExT wiTh meSseD UP'
print(txt.capitalize())  # Делает первую букву предложения заглавной
print(txt.title())  # Делает каждую первую букву заглавной
print(txt.upper())  # Делает все буквы большими
print(txt.lower())  # Делает все буквы маленькими


text = 'My LOng LoNg STRING'
string_index = text.lower().index('string')
print(text[:string_index].lower() + text[string_index:].upper())


msg = 'Hello world!'
msg = msg.replace('world', 'universe')
print(msg)


txt = ' admin '
# txt = txt.replace(' ', '')
txt = txt.strip()
print(txt)
txt = '"name"'
txt = txt.strip('"')
print(txt)



# TODO Строка <-> Список

my_string = 'some little text'
list_from_text = my_string.split()
print(list_from_text)

my_string = 'some,little,text'
list_from_text_2 = my_string.split(',')
print(list_from_text_2)


languages = ['Python', 'Java', 'Ruby']
print(languages)
# languages = ', '.join(languages)
print(languages)

print('Студент знает вот такие языки програмирования:', ', '.join(languages))


# TODO Фоматирование строки

a = 'one'
b = 'two'

print('First world is', a, ', second world is', b)

# Через контенацию строк
print('First world is ' + a + ', second world is ' + b)

# Через дедовский способ
my_text = 'First world is %s, second world is %s'
print(my_text % (a, b))

# string format
my_text = 'First world is {}, second world is {}'
print(my_text.format(a, b))

my_text = 'First world is {1}, second world is {0}'
print(my_text.format(a, b))

# f-string
my_text = f'First world is {a}, second world is {b}'
print(my_text)


template = 'Hello, {}!'
#print(f'Hello, {username}!')
username = input('What is yor name? ')
print(template.format(username))









