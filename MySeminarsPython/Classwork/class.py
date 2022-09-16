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

# b = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# count = 0
# for i in range(len(b)):
#     if b[i] == b[0]:
#         count += 1
#         if count == 2:
#             print(i+1)
#             break


# spisok = ['строка1', 'строка2', 'строка3', 'строка1']
# find_str = 'строка1'
# if spisok.count(find_str) < 2:
#     print(f'Второго вхождения строки {find_str} нет в заданном списке')
# else:
#     spisok1 = spisok[spisok.index(find_str) + 1:] # отрезаем первой вхождение
#     print(spisok1.index(find_str) + (len(spisok) - len(spisok1))) # ищем строку в оставшемся списке и прибавляем то количество элементов, которое отрезали

# t = {'a':'а', 'b':'б', 'v':'в', 'g':'г', 'd':'д', 'e':'е', 'zh':'ж', 'z':'з', 'i':'и', 'y':'й', 'k':'к', 'l':'л',
# 'm':'м', 'n':'н', 'o':'о',
# 'p':'п', 'r':'р', 's':'с','t':'т', 'u':'у', 'f':'ф', 'kh':'х', 'ts':'ц',
# 'ch':'ч', 'sh':'ш', 'shch':'щ',"'":'ь', 'ie':'э', 'yu':'ю', 'ya':'я'}
# a = list(input())
# for i in range(len(a)):
#     print(t[a[i]], end='')

# from random import randint

# a = int(input('Введите число '))
# list1 = []


# for i in range(a):
#     f = randint(-a, a)
#     list1.append(f)
# print(list1)
# print(f'Минимальное {min(list1)} и максимальное {max(list1)} числа')
def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Not quadratic equation")

d = discriminant(a, b, c)
if d < 0:
    return "No roots"
    elif d == 0:
            eturn f"One root x = {-b / (2 * a)}"
        else:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
        return f"Two roots: x1 = {x1}, x2 = {x2}"

    if __name__ == "__main__":
    print(solve_quadratic(5, -9, -2))
print(solve_quadratic(1, -4, 4))
print(solve_quadratic(1, -5, 9))
print(solve_quadratic(0, 1, 2))

inp = list(map(str, input().split()))
ans = list()
for i in inp:
    if i.isdigit():
        ans.append(i)
print(f'Максимум в строке равен {max(ans)}, минимум в строке равен {min(ans)}')