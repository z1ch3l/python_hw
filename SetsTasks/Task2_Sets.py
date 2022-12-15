"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""


testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
printSet = set()
arg = []
for smth in testList:
	try: printSet.add(smth)
	except:
		printSet.update(smth)
		n.append(smth)
if len(arg) == 0: print(smth)
else: print(False,arg,sep='\n')