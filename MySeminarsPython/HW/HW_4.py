# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# import math
# from math import pi

# d = float(input("Введите точность d: "))
# count = 0
# while d < 1:
#     d=d*10
#     count+=1
# print(round(pi,count))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# num = int(input("Введите число: "))
# i = 2 # первое простое число
# list = []
# old = num
# while i <= num:
#     if num % i == 0:
#         list.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print("Простые множители числа", old,':', *list)  
#     
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# first_list = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {first_list}")
# new_lst = []
# [new_lst.append(i) for i in first_list if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

# c задачами про многочлены не справилась