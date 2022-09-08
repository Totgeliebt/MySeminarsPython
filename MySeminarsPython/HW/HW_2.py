# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр (отсекаем минус, считаем все в плюс).
# Пример:
# 67,82 -> 23
# 0,56 -> 11
# 
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('input N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')
 
# Задайте список из n чисел 
# последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# n = int(input('Enter number: ')) 

# def sequence(n):

#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(sequence(n))
# print(round(sum(sequence(n))))

# 5. Реализуйте алгоритм перемешивания списка.

# from random import shuffle
# x = [[i] for i in range(10)]
# shuffle(x)
# print(x)


# line = 'оорррорррроооорооор'
# print(len(max(line.split('р'),key = len)))

line = 'ооррроррооор'
max_len = 0
while True:
    if 'о' in line:
        start = line.index('о')
    else:
        break
    if 'р' in line[start:]:
        end = line.index('р', start)
        max_len = max(max_len, len(line[start:end]))
    else:
        max_len = max(max_len, len(line[start:]))
        break
    line = line[end + 1:]
 
print(max_len)
