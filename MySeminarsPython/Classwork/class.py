# n = int(input('Insert fridges quality: '))
# inp = list()
# lookingFor = 'anton'
# for i in range(n):
#     inp[i] = str('Insert string: ')
#     for k in range(len(inp[i])):
#         if k == 'a':
# n = int(input())
# list1 = []
# for i in range(n):
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list1.append(i + 1)                   
# print(*list1)

# a = 'a1n1t1o1n1'
# if 'a' in a:
#     a = a[a.find('a'):]
#     if 'n' in a:
#         a = a[a.find('n'):]
#         if 't' in a:
#             a = a[a.find('t'):]
#             if 'o' in a:
#                 a = a[a.find('o'):]
#                 if 'n' in a:
#                      a = a[a.find('n'):]
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n

# result = list()
# n = int(input('введите число - '))
# for i in range(n):
#     result.append((-3)**i)
    
# for i in range(5):

# 	print((-3 )** i, end=' ')


# string1 = 'I love apples'
# string2 = 'apples'
# if len(string1) > len(string2):
#     print(string1.count(string2))  
# else:
#     print(string2.count(string1))  

# a = 'pyt'
# b = 'pythonpythonpython'
# count = 0
# for i in range(0, len(b) - len(a)):
#     if b[i:i + len(a)] == a:
#         count += 1 
# print(count)

# fname=input('file: ')
# f=open(fname, 'w')

# while True:
#     s=input()
#     if s=="":
#         break
#     f.write(s+ '\n')
# f.close()


# a=input()
# b=input()
# c = a+"-"+b
# m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
#     'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
#     'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
#     'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
#     'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
#     'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
#     'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
#     'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
#     'Спок-ящерица': 'Руслан'}

# print(m[c])

# finp = open('file.txt', 'r')
# count = 0
# for line in finp:
#     count += 1
#     print(len(line))
#     print(len(line.split()))

# print(f'количество строк в файле: {count}')
# finp.close()

# import time


# def GetRand(x, y):
#     count = y - x
#     result = int(time.time()) % count
#     return result + x


# print(GetRand(13, 222))
# print(time.time())

# inp = list(map(str, input('Введите список: ').split()))
# inp = list('njkmnkl', 'ijhkj', 123)
# N = int(input('Введите искомое число: '))
# if str(N) in inp:
#     print(f'Число {N} есть в списке')
# else:
#     print(f'Числа {N} в списке нет')

b = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
count = 0
for i in range(len(b)):
    if b[i] == b[0]:
        count += 1
        if count == 2:
            print(i+1)
            break


spisok = ['строка1', 'строка2', 'строка3', 'строка1']
find_str = 'строка1'
if spisok.count(find_str) < 2:
    print(f'Второго вхождения строки {find_str} нет в заданном списке')
else:
    spisok1 = spisok[spisok.index(find_str) + 1:] # отрезаем первой вхождение
    print(spisok1.index(find_str) + (len(spisok) - len(spisok1))) # ищем строку в оставшемся списке и прибавляем то количество элементов, которое отрезали