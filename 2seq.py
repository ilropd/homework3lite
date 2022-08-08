'''

Модуль реализует следующую логику:
Пользователь вводит любые цифры через запятую
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который
встречается в исходном списке только 1 раз)
Вывести новый список на экран
Порядок цифр в новом списке не важен
Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
Результат: 2, 4, 6, 9

(Дополнительно*) Предусмотреть что пользователь может использовать один из 3-х разделителей: запятую, точку с запятой,
слэш (1,2,3 1;2;3 1/2/3), но только какой то один 1,2;3/4 - так нельзя

'''

# импортируем библиотеку регулярных выражений
import re

# запрос ввода пользователем количества элементов в списске
digits = input('Введите элементы списка через запятую (например, 2,3,4,5,5,6,5,3,9): ')

digits = digits.replace(' ', '')    # убираем пробелы, которые пользователь мог случайно поставить

# заменим все любые символы, кроме цифр и '.' на ',' это поможет нам обойти ограничение с разнородными разделителями
# затем разобъем полученный сет на элементы по разделителю ','
digits = re.sub(r'[^\.0-9]', ',', digits).split(',')

# удалим в цикле пустые элементы
while '' in digits:
    digits.pop(digits.index(''))

# чтобы оставить только уникальные значения, приведем к типу множества
digits = set(digits)

print(*digits, sep=', ')    # выведем все значения множества через ','