"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""


def balls():
    ball = sum(colvo)
    if ball > 50 and ball <= 80:
        print('Наградить похвальной грамотой.')
    elif ball > 80:
        print('Наградить дипломом.')
    else:
        print('Выдать грамоту об участии.')


def sum(colvo):
    x = 0
    for i in range(colvo):
        ball = int(input('Введите баллы по предмету: '))
        x = x+ball
    print('Итоговый счёт: ', x)
    return x


x = 0
while x != 'стоп' :
    name = input('Введите имя: ')
    if name == 'стоп':
        x=name
        break
    colvo = input('Введите кол-во предметов: ')
    if colvo == 'стоп':
        x = colvo
        break
    else:
        colvo = int(colvo)
    balls()

