"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""


def imt_func():
   weight = int(input('Введите массу тела.'))
   height = int(input('Введите свой рост.'))
   index = weight / (height ** 2)
   return index

def imt_research(index):
    if index < 18.5:
        print('Недостаточный вес.')
    elif index >= 18.5 and index < 25:
        print('ИМТ в норме.')
    elif index > 25:
        print('Избыточный вес.')



imt_research(imt_func())