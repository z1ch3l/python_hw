while True:
    num = int(input('Цена: '))
    if num != 0:
        num2 = int(input('Скидка: '))
        print(num-(num/100*num2))
    else:
        break