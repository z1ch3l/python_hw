num = 3
start = input('Введите "game", чтобы начать игру. ')
while start == 'game' and num > 0:
    ans = str(input('Угадай число! '))
    if ans == 'off':
        break
    elif ans == '5':
        print('Вы выиграли билет на концерт!')
        break
    else:
        num -= 1
        print ('Попробуйте еще раз!')