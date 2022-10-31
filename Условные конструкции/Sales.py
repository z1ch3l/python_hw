a = int(input('Введите цену первого товара.'))
b = int(input('Введите цену второго товара.'))
c = int(input('Введите цену третьего товара.'))
if c > b and b > a and c > a:
    print('Акция!')
    print('К оплате:', (a+b+c)/2)
elif a > b and b > c and a > c:
        print('Акция!')
        print('К оплате:', (a+b+c)/2)
else:
    print('К оплате:', a+b+c)