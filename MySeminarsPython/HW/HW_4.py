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

# d = input('Введите число d указывающее степень округления числа pi ')
# d = d[2:len(d)]
# print(round(math.pi,len(d)))

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

# from random import randint

# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
#     koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
#     if k == 1:
#         ans.append(f'{koefs[i]}*x')
#     elif k == 0:
#         ans.append(f'{koefs[i]}')
#     else:
#         ans.append(f'{koefs[i]}*x**{k}')
#     flag = randint(0, 1)
#     if flag == 1:
#         ans.append('+')
#     elif flag == 0:
#         ans.append('-')
#     k -= 1

# ans.pop(-1)
# ans.append('=0')
# fout = open('output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()

ffile1 = open('file1.txt', 'r')
ffile2 = open('file2.txt', 'r')
ffile3 = open('file3.txt', 'w')
file1 = ffile1.readline()
file2 = ffile2.readline()
for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():
            ffile3.write(str(int(file1[i])+int(file2[i])))
        else:
            ffile3.write(str(file1[i]))
    else:
        ffile3.write(str(file1[i]))
ffile1.close
ffile2.close
ffile3.close