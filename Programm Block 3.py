#Задание1 Перевод C в F
#def temp(tc):
    #for i in range(tc):
        #tf = (9 / 5) * tc + 32
    #return tf
 
#def main():
    #tc = int(input('Введите температуру по Цельсию: '))
    #while tc >= -273:
        #tf = temp(tc)
        #print('Температура Цельсия', tc, 'равна', tf, 'градусам Фаренгейта.')
        #tc = int(input('Введите температуру по Цельсию: '))
 
#main()

#Задание1 Перевод C в F
#def cel2fah(cel):
    #fah = (9 / 5.0 * cel) + 32
    #return fah

#f1 = cel2fah(6.67)
#f2 = cel2fah(0)
#print (f1, f2)

#Задание2  Перевод F в C

#def fah2cel(fah):
    #cel = 5.0*(fah - 32) / 9
    #return cel

#c1 = fah2cel(32)
#c2 = fah2cel(44)
#print(c1, c2)

#Задание3
#def fun(minutes):
    #mn, sc = divmod(minutes, 5)
    #hr, mn = divmod(sc, 300)
    #return f"{mn}:{sc}:{hr}"
    
#Задание4
#from datetime import time
 
#current_time = time(24,00)
#print(current_time)     # 24:00:00 Day
 
#current_time = time(1440)
#print(current_time)     #1440 Minutes
 
#current_time = time(86400)
#print(current_time)     #86400 Houre

#Задание5
#import math
#x=4,5
#y=4,5
#a=9
#while y<9:
    #cos=y/x
    #y+=0.2
    #print('cos(a)',cos)

#Задание6
#print("Длины сторон треугольника:")
#a = float(input("a = "))
#b = float(input("b = "))
#c = float(input("c = "))
 
#flag = ''
#if a + b > c:
    #if a + c > b:
        #if b + c > a:
            #print("Треугольник есть")
        #else:
            #flag = 'a'
    #else:
        #flag = 'b'
#else:
    #flag = 'c'
 
#if flag != '':
    #print("Треугольника нет")
    #print("'%s' > суммы других" % flag)

#Задание7
#number = float(input("a = "))
#if number > 100
#if number  < 100:
    #print("False")
#else:
    #print("true")
#print("End")

#Задание8 Расчитать факториал
# n = int(input())
 
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
 
# print(factorial)

# Нажимаем ctrl / и зарабатывает команда (комментарий (#))

#Задача9
#import random
#while True:
    #i = random.randint(0, 10)
    #if int(input()) == i: print('True', i)
    #else: print('False', i)
  
 #Задача10 
#from random import randint
#n = randint(0, 100)
#i = 0
#while True:
    #a = int(input())
    #if a == n:
        #print('You win!')
        #break
    #if a < n:
        #print('загаданное число больше')
    #else:
        #print('загаданное число меньше')
    #i += 1
    #if i == 10:
        #print(f'Вы проиграли. Загаданное число {n}')
        #break
 
   #Задача10
          
#total = 0 
#while total < 100:  
 #num = int(input("Enter a number: "))  
#total = total + num 
#print("The total is ", total)


#Задача11 Код для считывания площади круга

#import math
#class circle():
    #def __init__(self, radius):
        #self.radius = radius
    #def area(self):
        #return math.pi * (self.radius**2)
    #def perimeter(self):
        #return 2 * math.pi * self.radius
 
#r = int(input("Введите радиус круга: "))
#obj = circle(r)
#print("Площадь круга:", round(obj.area(), 2))
#print("Длина окружности:", round(obj.perimeter(), 2))

