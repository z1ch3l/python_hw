price = int(input('Введите цену.'))
hours = int(input('Введите, который сейчас час.'))
if hours >=10 and hours <=12:
    print(price/2)
elif hours >=20 and hours <=22:
    print(price/4)
elif hours == 8 or hours == 9 or hours >=13 and hours <=19 :
    print(price)
else:
    print('Магазин сейчас закрыт.')
