mealchoose = input('Выбор приема пищи').lower()
if mealchoose == 'завтрак':
    print('  Рекомендуем попробовать Кашу')
else:
    print ('  Вы хотите плотно покушать?')
    mealamount = input('  ДА или НЕТ').lower()
    if mealamount == 'да':
        print('  Рекомендуем отведать плова')
    else:
        print('  Рекомендуем блюдо "Котлета с пюре"')
