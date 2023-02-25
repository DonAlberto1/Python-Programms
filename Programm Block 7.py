#Задача11:
# print(235.22/float(input()))
# gallon = 3.785
# mile = 1.6093
 
# MPG_index = float(input('Enter your MPG index: '))
# KmPL_index = MPG_index * mile / gallon # Показатель, сколько проедет авто км на 1 литре бензина
# LPKm_index = KmPL_index ** -1 # Показатель, сколько авто потратит литров на 1 км пробега
# LP100Km_index = LPKm_index * 100 # Показатель, сколько авто потратит литров на 100км пробега
# print(LP100Km_index)

#Задача12:
import math
# x1 = float(input("x1 - "))
# y1 = float(input("y1 - "))
# x2 = float(input("x2 - "))
# y2 = float(input("y2 - "))
# a = math.sqrt((x2-x1)**2+(y2-y1)**2)
# print('{:.3f}'.format(a), sep='')

#Задача13:
# summa = int(input('Сдача '))
# coins = [100, 50, 10, 5, 2, 1]
# for i in coins:
#     res, summa = divmod(summa, i)
#     if res:
#         print(f'{i} - {res}')

#Задача14:

# Преобразуем рост в футах и дюймах в сантиметры

# IN_PER_FT = 12
# CM_PER_IN = 2.54
# # Запрашиваем рост
# print("Укажите рост:")
# feet = int(input("Количество футов: "))
# inches = int(input("Количество дюймов: "))
# # Переводим в сантиметры
# cm = (feet * IN_PER_FT + inches) * CM_PER_IN
# # Вывод результата
# print("Рост в сантиметрах:", cm)

#Задача15:
# mapping, inp = {'mile': 1609, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001}, 
# input().split()
# print('%.2e' % (float(inp[0]) * float(mapping[inp[1]]) / float(mapping[inp[3]])))


#Задача16:
# import math
# def circle_length(radius):
#     return 2 * math.pi * radius
# def circle_area(radius):
#     return math.pi * radius * radius

#Примеры к Задаче16
# print(circle_length(5))
# 31.4159
# Пример 2
# Ввод
# Вывод
# print(circle_area(10))
# 314.159
# Пример 3
# Ввод
# Вывод
# main()
# 0.5
# 3.14159 0.7853975

#Задача17
# 1.890 кг
# 134С*]

# g = float(input("g - "))
# m = float(input("m - "))
# c = float(input("c - "))
# T = float(input("T - "))
# C = float(input("C - "))
# g = math.sqrt(1.890*g(4.186*T/g*c)*134)
# print(g)

#Задача18

# pi=22/7
# height = float(input('Height of cylinder: '))
# radian = float(input('Radius of cylinder: '))
# volume = pi * radian * radian * height
# sur_area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
# print("Volume is: ", volume)
# print("Surface Area is: ", sur_area)

#Задача19

#initial values

# t = 0
# h = 0

#ask user for initial speed and initial height

# b = float(input("What is the initial speed in metres per second?: "))
# c = float(input("What is the initial height in metres: "))

#calculate and display height 

# while h>=0:
#   h = round(-4.9*t**2+b*t+c, 2)
# if t==1:
#  print("After 1 second, the height is", h, "m.")
# elif h>0:
#  print("After", t, "seconds, the height is:", h, "m.")
# else:
#  print("After", t,"seconds, the ball is on the ground")
# t = t+1



#Задача19 Вариант 2

#Python's program to calculate the speed of an object when it hits the ground after being dropped.
##
 
# from math import sqrt
 
#Define the constant

# GRAVITY = 9.8  
 
#Read the input from user

# height  = float(input("Height from which object is dropped (in meters): "))
 
#Calculate the velocity

# velocity = sqrt(2 * GRAVITY * height)
 
#Display the result

# print("Object will hit the ground at %.2f m/s." % velocity)

#Задача20:

# p = float(input("p - "))
# cdot = float(input("cdot - "))
# V = float(input("V - "))
# T = float(input("T - "))
# r = float(input("r - "))
# print(r)
# print(p)
# print(cdot)
# print(T)
# print('p\cdot')
# V = float(input('r\cdot T'))
# print(V)

#Задача21:

# b = float(input("b - "))
# h = float(input("h - "))
# area = float(input("area - "))
# area = (b*h/2)
# print(area)

#Задача22:

# print("1-прямоугольник, 2-треугольник, 3-круг")
# figure = input("Выберите фигуру: ")
 
# if figure == '1':
#     print("Длины сторон прямоугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     print("Площадь: %.2f" % (a * b))
# elif figure == '2':
#     print("Длины сторон треугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = float(input("c = "))
#     p = (a + b + c) / 2
#     from math import sqrt
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print("Площадь: %.2f" % s)
# elif figure == '3':
#     r = float(input("Радиус круга R = "))
#     from math import pi
#     print("Площадь: %.2f" % (pi * r ** 2))
# else:
#     print("Ошибка ввода")

#Задача23:

# from math import tan, pi
# n = int(input())
# a = float(input())
# print(n*a*a/(4*tan(pi/n)))

#Задача24:

# from math import convert
# def convert_to_preferred_format(sec): 
#     sec = sec % (24 * 3600) 
#     hour = sec // 3600 
#     sec %= 3600 
#     min = sec // 60 
#     sec %= 60 
#     print("seconds value in hours:",hour) 
#     print("seconds value in minutes:",min) 
#     return "%02d:%02d:%02d" % (hour, min, sec) 
# n = 10000 
# print("Time in preferred format :-" 'convert(n)')
# print(convert(n))

#Задача25:

# from datetime import time
# from datetime import datetime
# from datetime import date
# def main():
#     ##Объект DATETIME
#     #получаем сегодняшнюю дату из класса datetime
#     today=datetime.now()
#     #выводим (today)
#     # Получаем текущее время
#     #t = datetime.time(datetime.now())
#     #выводим "The current time is", t
#     #день недели от 0 (понедельник) до 6 (воскресенье)
#     wd=date.weekday(today)
#     #Дни начинаются с 0 для понедельника
#     days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
#     print("Today is day number %d" % wd)
#     print("which is a " + days[wd])
 
# if __name__== "__main__":
#     main()

#Задача26:
# from datetime import date
# from datetime import time
# from datetime import datetime
# def main():
#     today = date.today()

#Задача27:
#Специальное примечание: алгоритм может указать дату в апреле. 
# Кроме того, если год является одним из четырех особых годов (1954, 1981, 2049 или 2076), вычтите из даты 7.
#Ваша программа должна выводить сообщение об ошибке, если пользователь вводит дату, выходящую за пределы допустимого диапазона.

# year = float(input("year - "))
# a = year % 19
# b = year % 4
# c = year % 7
# d = (19 * a + 24) % 30
# e = (2 * b + 4 * c + 6 * d + 5) % 7
# dateOfEaster = 22 + d + e

#Задача28:

# age = int(input())
# height = float(input())
# weight = float(input())
 
# if age < 10 or height < 0 or height > 3 or weight < 0 or weight > 500:    
#     print("Ошибочные входные данные")
# else:
#     bmi = weight / height ** 2  
#     bmi = round(bmi, 2)
    
#     if bmi < 18.5:
#         description = "недостаточной массой тела."            
#     elif bmi < 25:
#         description = "нормальной массой тела."            
#     elif bmi < 30:
#         description = "избыточной массой тела."  
#     else:          
#         description = "ожирением."
   
#     print("bmi=", bmi, "Вы относитесь к группе людей с", description)

#Задача29:
##Пример ввода данных в программу:
##Ввод: 
##Температура воздуха = 28
##Скорость ветра = 80
##Вывод: 30
##Расчет выполнен с использованием приведенной выше формулы:
##WCI = 13,12 + 0,6215 * (28) - 
##11.37 * (80)**0.16 + 
##0.3965 * 28 * 80**0.16
##Ввод: 
##Температура воздуха = 42
##Скорость ветра = 150
##Результат: 51
##Расчет выполнен с использованием приведенной выше формулы:
##WCI = 13,12 + 0,6215 * (42) - 11.37 * (150)**0.16 +0.3965 * 42 * 150**0.16
##Дальше программа Задачи 29, на Python, с комментариями
##Python program to calculate WCI

#Задача29

# import math
 
# # function to calculate WCI

# def WC(temp, wi_sp):
     
# # Calculating Wind Chill Index (Twc)
    
#     wci = 13.12+0.6215*temp- 11.37*math.pow(wi_sp, 0.16) + \
#           0.3965*temp*math.pow(wi_sp, 0.16)
#     return wci
     
# # Taking the Air Temperature (Ta)

# temp = 42
 
# # Taking the Wind Speed (v)

# wi_sp = 150
# print("The Wind Chill Index is", int(round(WC(temp, wi_sp))))

#3адача30
# C= float(input("C - "))
# F= float(input("F - "))
# print(float(input('C to F = ')) * (9 / 5) + 32)

#Задача30 Версия 2
#Программа на Python для преобразования температуры в градусы Цельсия и Фаренгейта и обратно.

# temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# degree = int(temp[:-1])
# i_convention = temp[-1]

# if i_convention.upper() == "C":
#   result = int(round((9 * degree) / 5 + 32))
#   o_convention = "Fahrenheit"
# elif i_convention.upper() == "F":
#   result = int(round((degree - 32) * 5 / 9))
#   o_convention = "Celsius"
# else:
#   print("Input proper convention.")
#   quit()
# print("The temperature in", o_convention, "is", result, "degrees.")

#3адача31
#Программа на Python для преобразования давления в килопаскалях в фунты на квадратный дюйм,---
#---миллиметр ртутного столба (мм рт. ст.) и атмосферное давление.

# kpa = float(input("Input pressure in in kilopascals> "))
# psi = kpa / 6.89475729
# mmhg = kpa * 760 / 101.325
# atm = kpa / 101.325
# print("The pressure in pounds per square inch: %.2f psi"  % (psi))
# print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
# print("Atmosphere pressure: %.2f atm." % (atm))

#3адача32

# a = input()
# b = input()
# c = input()
# d = input()
# summa = 0
# summa += int(a+b+c+d)
# print(summa)

#3адача33

# a = input()
# b = input()
# c = input()
# print ([[[(a, b, c), (a, c, b)], 
#   [None, (c, a, b)]],
#  [[(b, a, c), None], 
#   [(b, c, a), (c, b, a)]]])
# print([a < b][a < c][b < c])

#3адача34

# amount = float(input('Geben Sie die benötigte Brotmenge vom Vortag ein: '))
# price = 3.49 #Price for 1 Brotmenge
# sale = 60 #60% sale for Brot vom Votrag
# p = price * amount #Normalprice for Brot * amount
# s = p / 100 * sale #Sale for Brot vom Vortrag
# pp = p - s #Totalprice for Brot vom Vortrag mit Abziehung des Sales
# print = ('normaler Preis für frisches Brot: ', p)
# print = ('Der Rabatt für das gestrige Brot betragt {s} %')
# print = ('Der Gesamtpreis für den Kauf des gestrigen Brotes betragt:', pp)

##Код на Python для считывания различия между датами

# from datetime import datetime, timedelta
# def text_delta(t: timedelta) -> str:
#     if t < timedelta(minutes=1):
#         return "меньше минуты назад"
#     elif t < timedelta(hours=1):
#         return f"{t.total_seconds() // 60:.0f} минут назад"
#     elif t < timedelta(days=1):
#         return f"{t.total_seconds() // 3600:.0f} часов назад"
#     elif t < timedelta(days=30):
#         return f"{t.days} дней назад"
#     elif t < timedelta(days=365):
#         return f"{t.days // 30} месяцев назад"
#     else:
#         return f"{t.days // 365} лет назад"


# print(text_delta(datetime.now() - datetime(2021, 7, 14, 8, 0)))
# print(text_delta(timedelta(seconds=13)))
# print(text_delta(timedelta(minutes=13)))
# print(text_delta(timedelta(hours=13)))
# print(text_delta(timedelta(days=13)))
# print(text_delta(timedelta(days=30*3)))
# print(text_delta(timedelta(days=365*3)))


##Задача 35 Код для проверки количества и совмещения фруктов в корзине

# prices = {"banana": 4, "apple": 2, "orange": 1.5}
# stock = {"banana": 6, "apple": 0, "orange": 32}
# item = float(input("item - "))
# for item in prices:
#     print (item + ":")
#     print ("price:" + str(prices[item]))
#     print ("stock:" + str(stock[item]))
  
 