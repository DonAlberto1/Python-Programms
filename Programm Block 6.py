#Задача1
# first_name = input("Ваше имя: ")
# last_name = input("Ваша фамилия: ")
# mail_name = input("Ваша почта:")

# for i in range(10):

#    print(last_name + " " + first_name + " " + mail_name)

#Задача2
# name = input("Введите свое имя")
# print("Добрый день,", name, "!" )

#Задача3
# a = float(input('Введине длину комнаты (в метрах): '))
# b = float(input('Введите ширину комнаты (в метрах):  '))
# S = a * b
# print('Площадь комнаты: ' + str(S) + ' квадратных метров.')

#Задача4
# w = float(input('Введите ширину (в футах): '))
# l = float(input('Введите длину (в футах): '))
# S = (w * l) / 43560
# print('Площадь участка равна', S, 'акр')

#Задача5
# Вычисляем доход от сданной тары

# LESS_DEPOSIT = 0.10
# MORE_DEPOSIT = 0.25# Запрашиваем у пользователя количество бутылок каждого вида
# less = int(input("Сколько у вас бутылок объемом 1 литр и меньше? "))
# more = int(input("Сколько у вас бутылок объемом больше 1 литра? "))# Вычисляем сумму
# refund = less * LESS_DEPOSIT + more * MORE_DEPOSIT# Отобразим результат
# print("Ваша выручка составит $%.2f." % refund)

#Задача6
# Вычисляем налог и сумму чаевых в ресторане

# TAX_RATE = 0.05
# TIP_RATE = 0.18# Запрашиваем сумму счета у пользователя
# cost = float(input("Введите сумму счета: "))# Вычисляем сумму налога и чаевых
# tax = cost * TAX_RATE
# tip = cost * TIP_RATE
# total = cost + tax + tip# Отобразим результат
# print("Налог составил %.2f, чаевые – %.2f, общая сумма заказа: %.2f" % (tax, tip, total))

#Задача7
# Рассчитываем сумму первых n положительных чисел
# Запрашиваем значение числа n у пользователя

# n = int(input("Введите положительное число: "))# Рассчитываем сумму
# sm = n * (n + 1) / 2# Отобразим результат
# print("Сумма первых", n, "положительных чисел равна", sm)

#Задача8
# print(f'вес покупки: {int(input("Безделушек: ")) * 112 + int(input("Сувениров: ")) * 75} грамм')

#Задача9

# initial = deposit = 1_000_000
# percent = 100/4
# print(f'начальный депозит: {initial}, годовой процент: {percent*4}')

# for month in range(12):
#     income = deposit * percent / 12
#     deposit += income
#     print(f'месяц: {month+1}, доход: {income}, вклад: {deposit}')

# year_percent = (deposit - initial) / initial
# print(f'годовой процент c учётом капитализации составил: {year_percent*4}')

#Задача10

# import math
# print("Введите первое число")
# a = float(input())
# print("Введите второе число")
# b = float(input())
# result1 = math.pow(a+b,2)
# result2 = math.pow(a,2)+math.pow(b,2)
# print("Квадрат суммы = "+str(result1))
# print("Сумма квадратов = "+str(result2))






