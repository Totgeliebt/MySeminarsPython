# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# day_of_the_week = int(input('Введите число от 1 до 7 - '))
# if day_of_the_week == 6 or day_of_the_week == 7:
#     print('ДА!')
# else: 
#     print('Нет!')    

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# x = int(input('Введите координату по оси X -'))
# y = int(input('Введите координату по оси Y -'))
# if x>0 and y>0: 
#     print('1 четверть')
# elif x<0 and y>0:
#      print('2 четверть')
# elif x<0 and y<0:
#      print('3 четверть')
# elif x>0 and y<0: 
#     print('4 четверть')
# else: 
#     print('Введите координаты отличные от 0')

# Напишите программу, которая по заданному номеру четверти,показывает диапазон возможных 
# координат точек в этой четверти (x и y).

# x = int(input('Введите номер четверти от 1 до 4 - '))
# if x==1: 
#     print('x>0 and y>0')
# elif x==2:
#      print('x<0 and y>0')
# elif x==3:
#      print('x<0 and y<0')
# elif x==4 : 
#     print('x>0 and y<0')
# else: 
#     print('Введите корректное значение')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
#  в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# x_a = int(input('Введите координату X первой точки - '))
# y_a = int(input('Введите координату Y первой точки - '))
# x_b = int(input('Введите координату X второй точки - '))
# y_b = int(input('Введите координату Y второй точки - '))

# x_line = x_b-x_a
# y_line = y_b-y_a
# dist_quad = (x_line **2 + y_line**2)** 0.5

# print(round(dist_quad, 2))

# result = pow(dist_quad, 0.5)
# Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def logical_statement(x, y, z):
#     print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
#     return (not (x or y or z)) == (not x and not y and not z)
# if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
# logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
# logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
#     print("Истинно")
# else:
#     print("Ложно")

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not (x or y or z) == (not x and not y and not z))
            print(x,y,z)