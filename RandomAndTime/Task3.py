"""
На летней универсиаде будет проводиться по два забега. Чтобы соревнования были честными,
участники должны распределяться между забегами случайным образом.
Напишите программу, печатающую случайные номера забегов (1 или 2) до тех пор, пока не будет введено «off».
После генерации каждого номера должно печататься:
1) «Ваш номер: _».
2) «Участников в первом забеге: _», «Участников во втором забеге: _».
"""

from random import *

first_team = []
sec_team = []
while True:
    part = input("Участник: ")
    if part != "off":
        team = randint(1, 2)
        if team == 1:
            first_team.append(part)
        else:
            sec_team.append(part)
    else:
        break

print("Участников в первом забеге:", first_team)
print("Участников во втором забеге:", sec_team)