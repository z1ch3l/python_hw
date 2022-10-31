def schedule(spisok):
    dict_raspisaniye = {
        1: 'Hatha Yoga: \nВТ 17:00 - 18:00 \n ЧТ 17:00 - 18:00.',
        2: 'ВЕСЕЛЫЕ РЫБКИ: \nПН 07:00 - 08:00 \n СР 07:00 - 08:00.',
        3: 'TOTAL STRETCH: \nСБ 19:00 - 20:00 \n ВСКР 19:00 - 21:00'
    }
    # for i in spisok:
    #     print(dict_raspisaniye[i])
    return '\n'.join([dict_raspisaniye[i] for i in spisok])


def trener(spisok):
    dict_contact = {
        1: 'Тренер по Hatha Yoga: \nСветлана Вышкина \n+0 (000) 000 00-00.',
        2: 'Тренер по плаванью "ВЕСЕЛЫЕ РЫБКИ": \n Андрей Простатин \n+0 (000) 000 00-00.',
        3: 'Тренер по TOTAL STRETCH: \nНиколай Шпагатка \n+0 (000) 000 00-00'
    }
    # for i in spisok:
    #     print(dict_contact[i])
    return '\n'.join([dict_contact[i] for i in spisok])


    
def makse(task3):
    return f'Сумма к оплате: {task3 * 750}'


def contact_us():
    return 'Адрес фитнес-клуба: \nСупсехское шоссе, 39, строение 2 \nВремя работы клуба: \nс 7-00 до 24-00 \nВремя работы офиса продаж: \nс 9-00 до 20-00 \nежедневно без выходных \nТел. +7 (800) 100-28-41'


def sales():
    return 'Cейчас действует скидка на абонемент по услуге ВЕСЕЛЫЕ РЫБКИ. '