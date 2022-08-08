'''
Пять наиболее популярных методов, используемых для работы со списками
'''

import random


# создадим список с именами студентов
print('*** ИСХОДНЫЙ СПИСОК ***')

student_names = ['anna', 'ivan', 'pavel', 'maria', 'sergey']
print(student_names)

extra_names_list = ['maria', 'peter', 'anna', 'tamara', 'georgy', 'maria']    # создадим еще один список с именами

# метод .append(x) для внесения нового элемента в конец списка, на мой взгляд, самый популярный в работе со списками
# данный метод, на мой взгляд, популярнее похожего метода .insert(i, x), так как не требует знания содержания списка
# по индексам
print('\n*** БЛОК 1. Метод .append() ***')

student_names.append('olga')    # добавим в списк имен студентов имя 'olga'
print(student_names)

# не совсем метод, однако важный и популярный оператор для проверки вхождения элемента в список: in
# возвращает булевое значение True, если элемент входит в список и False, если не входит
print('\n*** БЛОК 2. Оператор in ***')

print(student_names)
name_number = random.randint(0, 5)    # случайным образом выберем одно из имен из дополнительного списка
check_name = extra_names_list[name_number]    # используем новое имя для проверки вхождения в список
print(f'Входит ли {check_name} в список имен студенов: {check_name in student_names}')

# также популярным методом работы со списками, на мой взгляд, является сортировка .sort([key=функция]), причем даже на
# самом базовом уровне сортировки по алфавиту просто с помощью .sort(), ооуществляющая сортировку "по алфавиту"
# чтобы отсортировать список "по убыванию", то ипользуется специальный параметр .sort(reverse=True)
# важно помнить, что данный метод не возвращает список с переставленными элементами, а меняет исходный список
print('\n*** БЛОК 3. Метод .sort() ***')

print(student_names)
student_names.sort()   # применим метод сортировки списка по алфавиту
print(student_names)

# один из популярных методов, на мой взгляд, .count(x), позволяющий определять количество элементов в списке для
# дальнейшей работы с ним
print('\n*** БЛОК 4. Метод .count() ***')

# в цикле рандомно добавим к нашему списку имена из дополнительного списка, а раз в нем есть имена, идентичные именам в
# нашем списке, мы сможем посчитать количество студентов с одним и тем же именем
for i in range(15):
    name_number = random.randint(0, 5)
    student_names.append(extra_names_list[name_number])
    i += 1

print(student_names)    # выведем обновленный список имен студентов
print(student_names.count('maria'))    # посчитаем сколько у нас студентов с именем 'maria'

# метод .remove() также может быть полезен в работе со списками при необходимости удалить определенное значение из
# списка, однко нужно помнить, что данный метод удаляет ПЕРВОЕ ВХОЖДЕНИЕ элемента. Поэтому если необходимо удалить все
# такие элементы, то лучше использовать данный метод совместно с циклом
print('\n*** БЛОК 5. Метод .remove() ***')

print(student_names)    # выведем обновленный список имен студентов

# используем метод .remove(), чтобы удалить из списка имен студентов 'maria' и убедимся, что исчезло только первое
# вхождение такого элемента
student_names.remove('maria')
print(student_names)

# чтобы удалить все упоминания 'maria' в списке, воспользуемся циклом, а затем снова выведем писок и убедимся, что
# исчезли все вхождения такого элемента
while 'maria' in student_names:
    student_names.remove('maria')
print(student_names)

# вероятно, одним из популярных методов работы со списками может быть индексирование (индекс первого вхождения)
# необходимого элемента в определенном месте списка, в этом случае может быть полезен метод .index(), где в качестве
# параметров задается искомый элемент, начало среза и конец среза

print('\n*** БЛОК 6. Метод .index() ***')

print(student_names)
find_name = 'tamara'
print(student_names.index(find_name, -5,-2) if find_name in student_names[-5:-2] else f'Элемент {find_name} в срезе не '
                                                                                    f'найден')
