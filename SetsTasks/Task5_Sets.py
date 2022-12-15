"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""

list_of_all = []
result_2 = {}
result_1 = set()

students = int(input("Пожалуйста, введите количество школьников: "))

while students > 0:
    n = int(input("Итог: количество школьников с общим языком: "))
    new_language = set()
    for i in range(n):
        s = input("Язык: ")
        new_language.add(s)
        if s in result_2:
            result_2[s] += 1
        else:
            result_2[s] = 1
        students = students - 1
    list_of_all.append(new_language)
    result_1 = result_1 | new_language
print(result_1)
print(list(filter(lambda x: result_2[x] == len(list_of_all), result_2.keys())))

new_language = set()
all_languages = set()
one_language = set()
students = int(input("Количество школьников: "))

while students > 0:
    n = int(input("Количество школьников с общим языком: "))
    students = students - n
    for i in range(n):
        lan = input("Язык: ")
        new_language.add(lan)
        all_languages.add(lan)
        one_language = all_languages & new_language

print(all_languages, one_language)