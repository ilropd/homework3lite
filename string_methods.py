'''
Пять наиболее популярных методов, используемых для работы со строками
'''

import random

print('*** ИСХОДНАЯ СТРОКА ***')
phrase = ' Cъешь же ещё этих мягких французских булок, да выпей чаю   '    # создадим исходную строку для работы
print(phrase)

# один из важных и популярных методов - определение длины строки с помощью метода len(), который возвращает количество
# символов в строке
print('\n*** БЛОК 1. Метод len() ***')

print(len(phrase))    # выведем длину исходной строки

# один из популярных методов, который используется при обработке и подготовке текста к анализу, это удаление лишних
# пробелов в начале и в конце строки с помощью метода .strip(), который возвращает новую строку без пробелов
# есть варианты данного метода для удаления пробелов в начале строки .lstrip() и в конце строки .rstrip()
print('\n*** БЛОК 2. Метод .strip() ***')

print(phrase)    # выведем исходную строку
print(len(phrase))    # выведем длину исходной строки

print(phrase.strip())    # удалим пробелы с обеих сторон строки
print(len(phrase.strip()))

print(phrase.lstrip())    # удалим пробелы в начале строки
print(len(phrase.lstrip()))    # выведем длину строки

print(phrase.rstrip())    # удалим пробелы в конце строки
print(len(phrase.rstrip()))    # выведем длину строки

# также важный метод - это разбиение строки по разделителю с помощью метода .split(), по умолчанию работает с пробелом,
# но может использовать для разбиения любой необходимый пользователю разделитель, возвращая список
# данный метод удобен при работе с файлами, сохраненными в формате csv
print('\n*** БЛОК 3. Метод .split() ***')

print(phrase.split(','))    # разделим строку по ","
print(type(phrase.split(',')))    # выведем тип данных

# один из популярных методов - приведение строки к единому формату, объединяет в себя сет методов, например, .lower(),
# .upper(), что является очень полезным при проверке ввода строки пользователем (приведение к единой форме)при условии,
# что регистр вводимых данных не имеет значения
print('\n*** БЛОК 4. Метод .upper() ***')

print(phrase.upper().strip())    # приведем все символы строки к верхнему регистру и удалим пробелы с обеих сторон

# один из самых востребованных методов работы со строками - это .format(), который позволяет максимально гибко
# настраивать вывод строки, исходя из требуемых параметров
print('\n*** БЛОК 5. Метод .format() ***')

student_names = ['Мария', 'Ольга', 'Катя']    # создадим список имен для дальнейшего случайного выбора

# вставим в строку случайное имя и сконкатенируем строки через пробел
print('Привет, {name}!'.format(name = student_names[random.randint(0, 2)]) + phrase, sep=' ')
