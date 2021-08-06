cashbox = int(input('Какова выручка фирмы - '))
costs = int(input('Какова издержка фирмы - '))
profit = cashbox - costs

if cashbox > costs:
    print('Ваша фирма работает в прибыль!\nОна составляет', "{0:.02f}".format(profit))
    rentabel = profit / cashbox
    print('Ваша рентабельность =',"{0:.02f}".format(rentabel))
    personal = int(input('Сколько сотрудников у вас работает?'))
    profit_to_one = profit / personal
    print ('Ваша прибыль на 1 сотрудника =',"{0:.02f}".format(profit_to_one))
elif cashbox == costs:
    print('У вас Дебет равен Кредиту!')
else: print('Вы в убытке Сер!')
