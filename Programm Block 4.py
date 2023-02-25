# Задание 1; Лекция 2
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

#Задание 2 Напечатать площадь окружности
# import math 
 
# def area_of_the_circle(Radius):  
#     area = Radius** 2 * math.pi 
#     return area 
 
# Radius = float(input("Please enter the radius of the given circle: ")) 
# print(" The area of the given circle is: ", area_of_the_circle(Radius)) 

#Задание 3 
# name = "Tom"  # переменной name равна "Tom"
# print(name)   # выводит: Tom
# name = "Bob"  # меняем значение на "Bob"
# print(name)   # выводит: Bob
# isMarried = False
# print(isMarried)    # False
# isAlive = True
# print(isAlive)      # True
# age = 21
# print("Возраст:", age)    # Возраст: 21
# count = 15
# print("Количество:", count) # Количество: 15
# a = 0b11
# b = 0b1011
# c = 0b100001
# print(a)    # 3 в десятичной системе
# print(b)    # 11 в десятичной системе
# print(c)    # 33 в десятичной системе
# a = 0o7
# b = 0o11
# c = 0o17
# print(a)    # 7 в десятичной системе
# print(b)    # 9 в десятичной системе
# print(c)    # 15 в десятичной системе
# height = 1.68
# pi = 3.14
# weight = 68.
# print(height)   # 1.68
# print(pi)       # 3.14
# print(weight)   # 68.0
# x = 3.9e3
# print(x)  # 3900.0
# x = 3.9e-3
# print(x)  # 0.0039
# complexNumber = 1+2j
# print(complexNumber)   # (1+2j)
# message = "Hello World!"
# print(message)  # Hello World!
# name = 'Tom'
# print(name)  # Tom
# text = ("Я Альберт "
#         "Приятно познакомиться")
# print(text)

#Задание 4
#В Python есть несколько стандартных типов данных:

#Numbers(числа)

#Strings(строки)

#Lists(списки)

#Dictionaries(словари)

#Tuples(кортежи)

#Sets(множества)

#Boolean(логический тип данных)

#Эти типы данных можно, в свою очередь, классифицировать по нескольким признакам:
#изменяемые(списки, словари и множества)
# неизменяемые(числа, строки и кортежи)
# упорядоченные(списки, кортежи, строки и словари)
#неупорядоченные(множества)

