# # Задача1; Программа перевода годов жизни Собаки в годы жизни Человека

# def calculator():
    
#     # Get dog age
#     age = input("Input dog years: ")

#     try:
#         # Cast to float
#         d_age = float(age)
#         # If user enters negative number, print message
#         if(d_age < 0):
#             print("Age can not be a negative number", age)
#         # Otherwise, calculate dog's age in human years
#         elif(d_age == 1):
#             d_age = 15
#         elif(d_age == 2):
#             d_age = 2 * 12
#         elif(d_age == 3):
#             d_age = 3 * 9.3
#         elif(d_age == 4):
#             d_age = 4 * 8
#         elif(d_age == 5):
#             d_age = 5 * 7.2
#         else:
#             d_age = 5 * 7.2 + (float(age) - 5) * 7
#         print("\n \t \'The given dog age", age, "is", d_age, "human years.'")
#     except ValueError:
#             print(age, "is an invalid age")

# calculator()

# Задача2: Программа для проверки буквы: Гласная она или согласная;

# l = input("Input a letter of the alphabet: ")

# if l in ('a', 'e', 'i', 'o', 'u'):
# 	print("%s is a vowel." % l)
# elif l == 'y':
# 	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
# else:
# 	print("%s is a consonant." % l) 

# # Задача3:

# year=int(input("Enter year to be checked:"))
# if(year%4==0 and year%100!= 0 or year%400==0):
#  print("The year is a leap year!")
# else:
#  print("The year isn't a leap year!")

# # Задача4 
# #Программа, которая предсказывает, кто выиграет игру.
# #Победит тот, у кого 2 очка ## Мы должны угадать число, сохраненное компьютером (0 - 5). ##Если вы угадаете, ваши очки увеличатся на 1.
# #Верните имя победившего участника в клин. пример игрока 1:

# # Задача4 Программа:

# class Solution:
#     def PredictTheWinner(self, A):
#         memo = {}
#         def maxscore(i,j):
#             if (i,j) in memo:
#                 return memo[i,j]
#             if i>j:
#                 return 0
#             #
#             sA = A[i] + min( maxscore(i+1,j-1), maxscore(i+2,j  ) ) # pick A[i] + min of the 2 possible upcoming turns (player 2 is smart)
#             sB = A[j] + min( maxscore(i  ,j-2), maxscore(i+1,j-1) )
#             score = max(sA,sB)
#             memo[i,j] = score
#             return score
#         p1 = maxscore(0,len(A)-1) # Score Player 1
#         return p1>=(sum(A)-p1) # p1 >= p2

# #Задача6; Программа для проверки четности или нечетности числа
# # Python program to check if the input number is odd or even.
# # A number is even if division by 2 gives a remainder of 0.
# # If the remainder is 1, it is an odd number.

# #Задача6;

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))

   





