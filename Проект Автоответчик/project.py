import funcs
print('Добро пожаловать! Ответьте на приведенные вопросы для получение более качественной консультации. ')
task1 = input('Введите ваши ФИО: ')
print('Список доступных услуг: \n 1. Hatha Yoga. \n 2. Веселые рыбки (занятия в бассейне). \n 3. TOTAL STRETCH.')
task2 = input('Каким(и) видом(ами) услуг из списка пользуетесь? ')
spisok = [i for i in task2 ]
task3 = int(input('Сколько занятий вы посетили суммарнo? '))
while True: 
    user_speak = input('Спасибо за ваши ответы! \nВведите свой запрос: ')
    if "расп" in user_speak:
        print(funcs.schedule(spisok))
    elif "трен" in user_speak:
        print(funcs.trener(spisok))
    elif "плат" in user_speak:
        print(funcs.makse(task3))
    elif "админ" in user_speak or "менедж" in user_speak or "связ" in user_speak:
        print(funcs.contact_us())
    elif "акц" in user_speak or "скид" in user_speak:
        print(funcs.sales())