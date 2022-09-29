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
# def discriminant(a, b, c):
#     return b ** 2 - 4 * a * c


# def solve_quadratic(a, b, c):
#     if a == 0:
#         raise ValueError("Not quadratic equation")

# d = discriminant(a, b, c)
# if d < 0:
#     return "No roots"
#     elif d == 0:
#             eturn f"One root x = {-b / (2 * a)}"
#         else:
#             x1 = (-b + d ** 0.5) / (2 * a)
#             x2 = (-b - d ** 0.5) / (2 * a)
#         return f"Two roots: x1 = {x1}, x2 = {x2}"

#     if __name__ == "__main__":
#     print(solve_quadratic(5, -9, -2))
# print(solve_quadratic(1, -4, 4))
# print(solve_quadratic(1, -5, 9))
# print(solve_quadratic(0, 1, 2))

# inp = list(map(str, input().split()))
# ans = list()
# for i in inp:
#     if i.isdigit():
#         ans.append(i)
# print(f'Максимум в строке равен {max(ans)}, минимум в строке равен {min(ans)}')


# Наибольший общий делитель
# def NOD(a,b):
#     if a % b == 0:
#         return b
#     else:
#         return NOD(b, a % b)

# print(NOD(58, 20))

# 1
# if a < b :
#     a, b = b, a

# while b!=0:
#     a, b = b, a % b

# print(a)

# 2
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a

# print(a)
# 3
# C = gcd(a,b)

# contains = lambda s, sample = 'ra': sample in s
# s = input()
# print(contains(s))

# import random
# def x(b=None):
#     if b is None:
#         b = random.randint(1, 10)

#     a=b+1
#     print(a)
# x_random1=x()
# x_random2=x()

# A = [1, 2, 3, 4, 6, 7]
# for i in range(1, len(A)):
#     if A[i]-1 != A[i-1]:
#         print(A[i-1]+1)

# def find_num(lst):
#     for i in range(1, len(lst)):
#         if lst[i] - lst[i - 1] > 1:
#             return i, lst[i] - 1
#     return -1, -1


# with open("data.txt", "r") as fin:
#     lst = [int(i) for i in fin.readline().split()]
#     print(lst)
#     pos, num = find_num(lst)
#     print(pos,num)
#     if (pos != -1):
#         lst.insert(pos, num)
#     print(lst)

# with open("words.txt", "r") as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if "абв" in word:
#                 words.remove(word)
#         sentence = " ".join(words)
#         print(sentence)


# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
# пример - 8 11 0 -23 140 1 => 11 -23
# print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))

# Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')


# b = filter(str.isalpha, a)
# c = filter(str.isdigit, a)

# print(*b)
# print(*c)

# 3. Преобразовать набора списков
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
# и потом вернуть в исходное состояние
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

# a,b,c = map(list,zip(users, ids, salary))
# print(a,b,c, sep="\n")
# a,b,c= map(list,zip(a,b,c))

# print(a,b,c, sep="\n")

# 4. Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

# list1 = [i for i in range(10, 100)]
# list2 = list(filter(lambda x: x%9 == 0, list1))
# list3 = sum(list(map(lambda x: x**2, list2)))
# print(list1)
# print(list3)

def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате cmv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

    # fields = ["id", "last_name", "first_name", "position", "phone_number", "salary"]

def read_csv() -> list:
    employee = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee

def find_employees_by_salary_range(employees: list) -> list:
    result = []
    lo, hi = get_salary_range()
    for employee in employees:
        if lo <= employee["salary"] <= hi:
            result.append(employee)
    return result

def write_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())

def run_work():
    employees  = read_csv()
    employee = {}
    while True:
        choice = show_menu()
        if choice == 1:             # find employee
            employee = find_employee(employees)
            if employee is None:
                no_employee_error()
            else:
                show_employee_info(employee)