'''

Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]

# 2 - количество случайных элементов
result = random.sample(numbers, 2)

print(result) # [5, 1]

После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'

Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь

В конце считаем количество правильных и неправильных ответов и предлагаем начать снова

'''

# импортируем библиотеку random, она поможет нам выбирать вопросы викторины случайным образом
import random

# импортируем библиотеку time для установления задержки между описанием викторины и первым вопросом
import time

# импортируем библиотеку регулярных выражений
import re

# ФОРМИРУЕМ ГРУППУ ИЗ 10 ЗНАМЕНИТОСТЕЙ
# дата рождения Бузовой О.И., правильный ответ "20.01.1986"
buzova = ('Назовите полную дату рождения самой осуждаемой, но все же известной телеведущей и, простигосподи, певицы '
          'современности Ольги Бузовой ---> ', '20.01.1986', 'Двадцатое января 1986 года')

# дата рождения Достоевского Ф.М., правильный ответ "11.11.1821"
dostoevsky = ('Назовите полную дату рождения руского писателя и классика мировой литературы Федора Михайловича '
              'Достоевского ---> ', '11.11.1821', 'Одиннадцатое ноября 1821 года')

# дата рождения Елизаветы II, правильный ответ "21.04.1926"
elizabeth = ('Назовите полную дату рождения царствующей Королевы Великобритании, любимицы жителей Туманного Альбиона и '
             'невероятно стойкой женщины Елизаветы II ---> ', '21.04.1926', 'Двадцать первое апреля 1926 года')

# дата рождения Ганди М., правильный ответ "02.10.1869"
gandhi = ('Назовите полную дату рождения индийского политического и общественнго деятеля, идеолога философии ненасилия, '
          'одного из руководителей движения за независимость Индии от Великобритании Махатмы Ганди ---> ', '02.10.1869',
          'Второе октября 1869 года')

# дата рождения Капицы П.Л., правильный ответ "08.07.1894"
kapitsa = ('Назовите полную дату рождения легендарного советского физика, лауреата Нобелевкой премии, известного '
           'изобретателя и новатора Петра Леонидовича Капицы ---> ', '08.07.1894', 'Восьмое июля 1984 года')

# дата рождения Кеннеди Д., правильный ответ "29.05.1917"
kennedy = ('Назовите полную дату рождения 35-го президента США, убитого в 1963 году на 47 году жизни, Джона Кеннеди ---> ',
           '29.05.1917', 'Двадцать девятое мая 1917 года')

# дата рождения Пресли Э., правильный ответ "08.01.1935"
presley = ('Назовите полную дату рождения короля рок-н-ролла и одного из самых успешных коммерческих исполнителей Элвиса '
           'Пресли ---> ', '08.01.1935', 'Восьмое января 1935 года')

# дата рождения Ремарка Э.М., правильный ответ "22.06.1898"
remarque = ('Назовите полную дату рождения немецкого писателя, чьи книги запретили и сжигали национал-социалисты, Эриха '
            'Марии Ремарка ---> ', '22.06.1898', 'Двадцать второе июня 1898 года')

# дата рождения Солженицына А.И., правильный ответ "11.12.1918"
soldjenitsyn = ('Назовите полную дату рождения русского писателя, драматурга, уникального политического и общественного '
                'деятеля Александра Исаевича Солженицына ---> ', '11.12.1918', 'Одиннадцатое декабря 1918 года')

# дата рождения Тетчер М., правильный ответ "13.10.1925"
thatcher = ('Назовите полную дату рождения "железной леди" Парламента Великобритании, лидера Консервативной партии '
            'Англии, баронессы Маргарет Тетчер ---> ', '13.10.1925', 'Тринадцатое октября 1925 года')

# соберем все переменные со знменитостями в единый кортеж
allppl = (buzova, dostoevsky, elizabeth, gandhi, kapitsa, kennedy, presley, remarque, soldjenitsyn, thatcher)

# задаем булевую переменную для входа в игру и возможности дальнейшего повтора
wannaplay = True

number_question = 5

# пока желание играть истинно, проводим викторину
while wannaplay:
    right_count = 0    # счетчик количества правильных ответов
    wrong_count = 0    # счетчик количества НЕправильных ответов

    # выводим вводное обращение к пользователю с пояснениями основного правила
    print('Мы спросим вас даты рождения 5 знаменитых личностей, а вы должны отвечать в формате ДД.ММ.ГГГГ, например, '
          '"01.05.1999". Итак, начнем игру.')

    # в этот список вводим порядковый номер вопроса, чтобы избежать повторений
    random_list = []

    # проходимся циклом и задаем вопросы
    for i in range(number_question):

        # перед тем как задавать первый вопрос сделаем задержку на 3 секунды, чтобы пользователь прочитал описание
        # викториины
        if i == 0:
            time.sleep(3)

        # случайным образом выбираем вопрос из нашего кортежа allppl, ограничиваем разброс от 0 до 9
        # так как у нас всего 10 вопросов
        question = random.randint(0,9)

        # сравниваем полученное значение с нашим списком вопросов, которые уже задавалиь
        # если такой вопрос уже задавался, то выбираем новое случайное число
        while question in random_list:
            question = random.randint(0,9)

        # если такой вопрос еще не задавали и его нет в нашем списке, то добавляем в список
        random_list.append(question)

        # задаем вопрос нашему пользователю, используя срезы кортежа allppl, где первое значение - это номер переменной
        # в кортеже, а второй значит, что нужно взять первый элемент нашей переменной - текст с вопросом
        answer = (input('\nВопрос №{qn}. {q}'.format(qn=i+1, q=allppl[question][0])))

        # проверяем ввод пользователя: если он вводит что-то кроме даты - повторяем вопрос и просим быть внимательнее
        # также делаем простую проверку на правильность формата ввода за счет подсчета количества символов в ответе
        while len(answer) != 10:
            print('БУДЬТЕ ВНИМАТЕЛЬНЫ! При вводе ответа используйте формат ДД.ММ.ГГГГ. Если день рождения 1 мая 1999 '
                  'года, то необходимо написать 01.05.1999')
            answer = (input('{q}'.format(q = allppl[question][0])))

        # проверяем ответ пользователя, используя срезы кортежа allppl, где первое значение - это номер переменной
        # с вопросом, а второй значит, что нужно взять втрой элемент нашей переменной - ответ на вопрос
        # чтобы избежать проблем с символами, все символы, кроме цифр, будут заменяться на '.'
        if re.sub(r'[\D]', '.', answer) == allppl[question][1]:
            print('Верно.')
            right_count += 1    # если пользователь ответил правильно, то счетчик правильных ответов увеличивается на 1
        else:
            print(f'Неверно. Правильный ответ: {allppl[question][2]}.')
            wrong_count += 1    # если пользователь ответил НЕправильно, то счетчик НЕправильных ответов увеличивается на 1

        i += 1    # делаем шаг в цикле вопросов

    # после окончания цикла вопросов выводим статистику по викторине: количество заданных вопросов, количество и процент
    # правильных ответов, количство и процент НЕправильных ответов. Процентное значение округляем до двух знаков после
    # запятой для облегчения восприятия и создания ощущения высокой точности расчета.
    print('Всего задано вопросов: {total}. Из них правильных ответов: {right} или {right_perc}%. И неправильных ответов '
          '{wrong} или {wrong_perc}%.'.format(total=number_question, right=right_count,
                                              right_perc=round(right_count*100/number_question, 2),
                                              wrong=wrong_count,
                                              wrong_perc=round(wrong_count*100/number_question, 2)))

    # в соответтвии с ТЗ спрашиваем пользователя о желании сыграть еще
    # чтобы нивелировать проблемы с интерпретацией ввода и избежать крушения программы при вводе "Да" вместо "да",
    # приводим любые введенные значения к нижнему регистру с помощью фунциии .lower()
    play_again = input('\nХотите сыграть еще? Ответьте да/нет: ').lower()

    # создадим возможные допольнительные варианты ответа "да", включая опечатку типа "lf", если пользователь забыл
    # переключить раскладку клавиатуры
    yes_list = ['да', 'д', 'yes', 'y', 'lf','l', '1', 'true']

    # проверяем ответ пользователя, заодно убираем пробелы в начале и в конце строки ввода с помощью функции .strip(),
    # чтобы избежать крушения программы из-за возможных пробелом, введенных полььзователем
    if play_again.strip() in yes_list:    # проверяем, есть ли ответ есть в списке ответов типа "да"
        wannaplay = True    # если ответ есть в списке типа "да", то переменная wannaplay остается истиной и игра продолжается
        print('\nНовый раунд.')    # выводим сообщение о новом раунде игры
    else:
        wannaplay = False    # если ответа нет в списке типа "да", то переменная wannaplay становится ложной и игра заканчивается
        print('Было приятно поиграть. Пока!')    # выводим сообщение об окончании игры