a=int(input('Введите целое положительное число -'))
b = a % 10
goal = b
while a > b:
    a = a // 10
    b = a % 10
    goal = max(goal,b)
print('Самое большая цифра в цисле - ',goal)