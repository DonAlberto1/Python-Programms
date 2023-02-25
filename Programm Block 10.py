# #  Задача 38

# a=int(input("Введите кол-во сторон:"))
# if a==3:
#     print("треугольник")
# elif a==4:
#      print("четырехугольник")
# elif a==5:
#      print("пятиугольник")
# elif a==6:
#      print("шестиугольник")
# elif a==7:
#      print("семиугольник")
# elif a==8:
#      print("восьмиугольник")
# elif a==9:
#      print("девятиугольник")
# elif a==10:
#      print("десятиугольник")
# else:
#      print("ошибка")

# #  Задача 39

# a = input().lower()
# if a == 'январь' or a == 'март' or a == 'май' or a == 'июль' or a == 'июль' or a == 'август' or a == 'октябрь' or a == 'декабрь':
#     print(31)
# elif a == 'февраль':
#     print('28 или 29')
# elif a == 'апрель''июнь''сентябрь''ноябрь':
#     print(30)


# #  Задача 40

# decibels = float(input("Enter the number of decibels: "))
# ('40  < > 0  0 > < 40:')
# print ('quieter than a quiet room.')
		
# ('40  == == 40:')
# print ('about the same as a quiet room.')
	
# ('70  < > 40  40 > < 70:')
# print ('quieter than an alarm clock.')
# ('70  == == 70:')
# print ('about the same as an alarm clock.')
		
# ('106  < > 70  70 > < 106:')
# print ('quieter than a lawn mower.')
	
# ('106  == == 106:')
# ('about the same as a lawn mower.')
	
# ('130  < > 106  106 > < 130:')
# print (" quieter than a jackhammer.")
		
# ('130  == == 130:')
# print('about the same as a jackhammer.')
		
# ('130 > > 130:')
# print ('way too loud.')
    
# ifelse: print("Please enter a correct data value.")
# print('Your sound level is')

# # Задача41

# def check_triangle(a, b, c):
#     if a == b == c:
#         return "Равностороний"
#     elif a == b or a == c or b == c:
#         return "Равнобедренный"
#     else:
#         return "Разносторонний"

# # Задача42
# math = input("math")
# def freq_to_note(freq):
#     notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

#     note_number = 12 * math.log2(freq / 440) + 49 
#     note_number = round(note_number)
        
#     note = (note_number - 1 ) % len(notes)
#     note = notes[note]
    
#     octave = (note_number + 8 ) // len(notes)
    
#     return note, octave

# #Задача43
# from math import log2, pow

# A4 = 440
# C0 = A4*pow(2, -4.75)
# name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
 
# def pitch(freq):
#  h = round(12*log2(freq/C0))
#  octave = h // 12
#  n = h % 12
#  return name[n] + str(octave)

# #Задача44

# def no_notes(a):
#       Q = [500, 200, 100, 50, 20, 10]
# x = 0
# for i in range(6):
#     q = Q[i]
#     x += int(a / q)
#     a = int(a % q)
# if a > 0:
#     x = -1
#     "return" (x)
# print(no_notes(880))
# print(no_notes(1000))

# #Задача44

# def main():
#     notes = {"1"  : "George Washinton",
#              "2"  : "Thomas Jefferson",
#              "5"  : "Abraham Lincoln",
#              "10" : "Alexander Hamilton",
#              "20" : "Andrew Jackson",
#              "50" : "Ulysses S. Grant",
#              "100": "Benjamin Franklin"}
     
#     value = input("Please enter the value of an US dollar note: ")
#     if value not in notes:
#         print("Sorry that is not a valid US dollar note")
#     else:
#         print("On that note you will find", notes[value])
 
            
# if __name__ == '__main__':
#     main()

# #Задача44




# #Задача46

# letter=input('Please enter the letter-> ')
# digit=int(input('Please enter the digit-> '))

# letters_list=['a','b','c','d','e','f','g','h']
# letters_list_black=['a','c','e','g']
# letters_list_white=['b','d','f','h']
# digits_list=range(1,9)
# chess_desk_letter=[]
# chess_desk_number=[]

# for letter_checking in letters_list:
#         if letter==letter_checking:
#                 chess_desk_letter.append(letter)
#                 break
# else:
#         print('Not in list, use A-H')
# for digit_checking in digits_list:
#         if digit==digit_checking:
#                 chess_desk_number.append(digit)
#                 break
# else:
#         print('Not in list use 1-8')
        
# if chess_desk_letter[0] in letters_list_black:
#         print(chess_desk_letter,chess_desk_number)
#         color=(chess_desk_number[0]%2)
#         if color==0:
#                 print('White')
#         else:
#                 print('Black')
# elif chess_desk_letter[0] in letters_list_white:
#         print(chess_desk_letter,chess_desk_number)
#         color=(chess_desk_number[0]%2)
#         if color==0:
#                 print('Black')
#         else:
#                 print('White')

# #Задача47
# month = input("Input the month (e.g. January, February etc.): ")
# day = int(input("Input the day: "))

# if month in ('January', 'February', 'March'):
# 	season = 'winter'
# elif month in ('April', 'May', 'June'):
# 	season = 'spring'
# elif month in ('July', 'August', 'September'):
# 	season = 'summer'
# else:
# 	season = 'autumn'

# if (month == 'March') and (day > 19):
# 	season = 'spring'
# elif (month == 'June') and (day > 20):
# 	season = 'summer'
# elif (month == 'September') and (day > 21):
# 	season = 'autumn'
# elif (month == 'December') and (day > 20):
# 	season = 'winter'

# print("Season is",season)

# #Задача48

# date=int(input("Введите день рождения:"))

# month=int(input("Введите месяц рождения:"))

# year=int(input("Введите год рождения:"))


# if (date>=21 and date<=31 and month==3) or( month==4 and date>=1 and date<=19):

#    print("Знак зодиака:Овен")

# elif (date>=20 and date<=30 and month==4) or( month==5 and date>=1 and date<=20):

#    print("Знак зодиака:Телец")

# elif (date>=21 and date<=31 and month==5) or( month==6 and date>=1 and date<=21):

#    print("Знак зодиака:Близнецы")

# elif (date>=22 and date<=30 and month==6) or( month==7 and date>=1 and date<=22):

#    print("Знак зодиака:Рак")

# elif (date>=23 and date<=31 and month==7) or( month==8 and date>=1 and date<=22):

#    print("Знак зодиака:Лев")

# elif (date>=23 and date<=31 and month==8) or( month==9 and date>=1 and date<=22):

#    print("Знак зодиака:Дева")

# elif (date>=23 and date<=30 and month==9) or( month==10 and date>=1 and date<=23):

#    print("Знак зодиака:Весы")

# elif (date>=24 and date<=31 and month==10) or( month==11 and date>=1 and date<=22):

#    print("Знак зодиака:Скорпион")

# elif (date>=23 and date<=30 and month==11) or( month==12 and date>=1 and date<=21):

#    print("Знак зодиака:Стрелец")

# elif (date>=22 and date<=31 and month==12) or( month==1 and date>=1 and date<=20):

#    print("Знак зодиака:Козерог")

# elif (date>=21 and date<=31 and month==1) or( month==2 and date>=1 and date<=18):

#    print("Знак зодиака:Водолей")

# elif (date>=19 and date<=29 and month==2) or( month==3 and date>=1 and date<=20):''

# #Задача49


# # Determine the animal associated with a year according to the Chinese zodiac.
# #
# # Read a year from the user
# year = int(input("Enter a year: "))
# # Determine the animal associated with that year
# if year % 12 == 8:
#     animal = "Dragon"
# elif year % 12 == 9:
#     animal = "Snake"
# elif year % 12 == 10:
#     animal = "Horse"
# elif year % 12 == 11:
#     animal = "Sheep"
# elif year % 12 == 0:
#     animal = "Monkey"
# elif year % 12 == 1:
#     animal = "Rooster"
# elif year % 12 == 2:
#     animal = "Dog"
# elif year % 12 == 3:
#     animal = "Pig"
# elif year % 12 == 4:
#     animal = "Rat"
# elif year % 12 == 5:
#     animal = "Ox"
# elif year % 12 == 6:
#     animal = "Tiger"
# elif year % 12 == 7:
#     animal = "Hare"
# # Report the result
# print("%d is the year of the %s." % (year, animal))

# #Задача50
# pd = int(input("Enter a pd: "))
# plt = int(input("Enter a plt: "))
# means = int(input("Enter a means: "))
# stats = int(input("Enter a stats:"))
# variance = int(input("Enter a variance:"))
# sp = int(input("Enter a sp:"))
# def load_data( fname ):
#     return pd.read_csv('data/ch02/' + fname, '\t')

# def ex_2_1():
#     return load_data('dwell-times.tsv').head()
# def ex_2_2():
#     load_data('dwell-times.tsv')['dwell-time'].hist(bins=50)
#     plt.xlabel('Время пребывания, сек.')
#     plt.ylabel('Частота')
#     plt.show()   
# def ex_2_3():
#     load_data('dwell-times.tsv')['dwell-time'].plot.hist(bins=20, logy=True)
#     plt.xlabel('Время пребывания, сек.')
#     plt.ylabel('Логарифмическая частота')
#     plt.show()  
# def ex_2_4():
#     ts = load_data('dwell-times.tsv')['dwell-time']
#     print('Среднее:               ', ts.mean())    
#     print('Медиана:               ', ts.median())
#     print('Стандартное отклонение:', ts.std())
# def with_parsed_date(df):
#     '''Привести поле date к типу date-time'''
#     df['date'] = pd.to_datetime(df['date'], errors='ignore')
#     return df

# def filter_weekdays(df): 
#     '''Отфильтровать по будним дням'''
#     return df[df['date'].index.dayofweek < 5]  # понедельник..пятница

# def mean_dwell_times_by_date(df):
#     '''Среднесуточные времена пребывания'''
#     df.index = with_parsed_date(df)['date']
#     return df.resample('D').mean()  # перегруппировать  

# def daily_mean_dwell_times(df):
#     '''Средние времена пребывания с фильтрацией - только по будним дням'''
#     df.index = with_parsed_date(df)['date']
#     df = filter_weekdays(df)
#     return df.resample('D').mean()
# def ex_2_5():
#     df  = load_data('dwell-times.tsv')    
#     mus = daily_mean_dwell_times(df)
#     print('Среднее:                ', float(means.mean()))    
#     print('Медиана:                ', float(means.median()))
#     print('Стандартное отклонение: ', float(means.std()))
# def ex_2_6():
#     df = load_data('dwell-times.tsv')
#     daily_mean_dwell_times(df)['dwell-time'].hist(bins=20)
#     plt.xlabel('Время пребывания по будним дням, сек.')
#     plt.ylabel('Частота')
#     plt.show()
# def ex_2_7():
#     '''Подгонка нормальной кривой поверх гистограммы'''
#     df = load_data('dwell-times.tsv')
#     means = daily_mean_dwell_times(df)['dwell-time'].dropna() 
#     ax = means.hist(bins=20, density=True)
#     xs = sorted(means)    # корзины
#     df = pd.DataFrame()
#     df[0] = xs
#     df[1] = stats.norm.pdf(xs, means.mean(), means.std())
#     df.plot(0, 1, linewidth=2, color='r', legend=None, ax=ax)
#     plt.xlabel('Время пребывания по будним дням, сек.')
#     plt.ylabel('Плотность')    
#     plt.show()
#     def variance(xs):
#         '''Несмещенная дисперсия (варианс) при n <= 30'''
#     x_hat = xs.mean() 
#     n = len(xs)
#     n = n-1 if n in range(1, 30) else n  
#     square_deviation = lambda x : ('(x – x_hat) ** 2') 
#     return sum( map(square_deviation, xs) ) / n

# def standard_deviation(xs):
#     return sp.sqrt(variance(xs))

# def standard_error(xs):
#     return standard_deviation(xs) / sp.sqrt(len(xs))
    
