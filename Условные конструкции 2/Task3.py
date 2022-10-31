login = input()
disallow_sym = '=?*^$№@_ '
count = 0
for i in login:
    if i in disallow_sym:
        print('Использован недопустимый символ: ', i)
        break
    else:
        count += 1
    if count == len(login):
        print('Все хорошо')
        break
