# print("Hello world!")

# Задача №1
# a = input()
#
# print( a[:a.find('h')] + a[a.rfind('h') +1:])

# Задача №2

# s = input()
# a = s[:s.find('h')]
# b = s[s.find('h'):s.rfind('h') + 1]
# c = s[s.rfind('h') + 1:]
# s = a + b[::-1] + c
# print(s)

# Задача №3

# s = "11 23 44 55 23 22"
# str1 = input("Введите заменяемую подстроку: ")
# str2 = input("Новая подстрока: ")
# print(s.replace(str1, str2))

# Задача №4

# s = """
# Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели
# """
# col = 0
# for i in s.lower().split():
#     if i.startswith("е"):
#         col += 1
# print(f"Количество слов: {col}")

# 10.02.23
# Задача №1
# import re
# def validate_name(name):
#     return re.findall(r'^[a-z\d@_-]{6,18}$', name, re.IGNORECASE)
#
# print(validate_name('_my-p@sswOrd'))

# Задача №2
# s = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
# reg = r"[0-3][0-9]/[0-1][0-9]/\d{4}"
# print(re.findall(reg, s))


# 12.02.23.
# Задача 1.
# import re
# s = "+7 499 456-45-78, +7 4994564578, 7 (499) 456 45 78, 7 (499) 456-45-78"
# r = r"\+?(?:7|\d){1}\s?\(?\d{3}\)?\s?\d{3}\s?\-?\d{2}\s?\-?\d{2}"
# print(re.findall(r, s))

# Задача 2.
# def CalcSumNegativeNumbers(A):
#     if A == []:
#         return 0
#     else:
#         count = CalcSumNegativeNumbers(A[1:])
#     if A[0]<0:
#             count = count + 1
#     return count
#
# S = [ -2, 3, 8, -11, -4, 6 ]
# n = CalcSumNegativeNumbers(L)
# print("n = ", n)

# 17.02.23
# def binary_search(lst, search_item):
#     low = 0
#     high = len(lst) - 1
#     search_res = False
#
#     while low <= high and not search_res:
#         middle = (low + high) // 2
#         guess = lst[middle]
#         if guess == search_item:
#             search_res = True
#         if guess > search_item:
#             high = middle - 1
#         else:
#             low = middle + 1
#     return search_res
#
#
# lst = [6, 10, 14, 15, 34, 39, 42, 63, 71, 97]
# value = 15
# result = binary_search(lst, value)
# if result:
#     print("Элемент найден!")
# else:
#     print("Элемент не найден.")

#№17.02.23
# from random import randint
#
# def binary_search(s, item):
#     found = False
#     first = 0
#     last = len(s) - 1
#     found = False
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#     return found
#
# a = [randint(1, 100) for i in range(10)]
# print(a)
# a.sort()
# n = int(input("Введите число: "))
# if binary_search(a, n):
#     print(f"Число {n} в списке присутствует")
# else:
#     print(f"Число {n} в списке отсутствует")

# 19.02.23

# from random import randint
#
# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [randint(1, 100) for i in range(10)]
# print(lst)
# n = int(input("Введите число: "))
# if seq_search(lst, n):
#     print(f"Число {n} в списке присутствует")
# else:
#     print(f"Число {n} в списке отсутствует")


#  ---------2--------

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open("text2.txt", "r")
# read_f = f.readlines()
# print(read_f)
# pos = int(input("Введите индекс удаляемой строки: "))
# for i in range(len(read_f)):
#     print(read_f)
#     if i == pos:
#         read_f[i] = ""
# print(read_f)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_f)
# f.close()

#  ---------3--------

# a = [5, 9, 6, 7]
# b = [3, 11, 8]
# c = [2, 4]
# d = [10, 1, 12]
# lst = a + b + c + d
#
#
# def bubble(array, n):
#     if n == 1:
#         for i in range(len(array) - 1):
#             for j in range(len(array) - i - 1):
#                 if array[j] < array[j + 1]:
#                     array[j], array[j + 1] = array[j + 1], array[j]
#     elif n == 2:
#         for i in range(len(array) - 1):
#             for j in range(len(array) - i - 1):
#                 if array[j] > array[j + 1]:
#                     array[j], array[j + 1] = array[j + 1], array[j]
#
#
# print(lst)
# s = int(input("Выберите способ сортировки, где:\n 1 - сортировка по убыванию\n 2 - сортировка по возрастанию\n -> "))
# bubble(lst, s)
# print(lst)
#
#
# def seq_search(lst1, item):
#     y = 0
#     found = False
#     while y < len(lst1) and not found:
#         if lst1[y] == item:
#             found = True
#         else:
#             y += 1
#     return found
#
#
# pos = int(input("Введите значение для поиска: "))
# if seq_search(lst, pos):
#     print(f"Значение {pos} найдено")
# else:
#     print(f"Значение {pos} не найдено")

# 24.02.23
# with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
#     f1.write("Текст файла № 1")
#     f2.write("Текст файла № 2")
#
# with open("file3.txt", "a") as f3, open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
#     for line in f1:
#         f3.write(line)
#     f3.write("\n")
#     for line1 in f2:
#         f3.write(line1)

#  -----2------

# import os
#
#
# def file_found(ff):
#     cwd = os.getcwd()
#     x_file = os.path.join(cwd, ff)
#     if os.path.exists(x_file):
#         print(os.path.basename(x_file), os.path.dirname(x_file),
#         "- last access time", os.path.getatime(x_file), "sec")
#     else:
#         print("file not found")
#
#
# fl = input("Введите название файла: ")
# file_found(fl)

# 26.02.23
# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#         print("Длина прямоугольника:", self.length)
#         print("Ширина прямоугольника:", self.width)
#
#     def s_rectangle(self):
#         s = self.length * self.width
#         print("Площадь прямоугольника:", s)
#
#     def rectangle_perimeter(self):
#         p = 2 * (self.length + self.width)
#         print("Периметр прямоугольника:", p)
#
#     def rectangle_hypotenuse(self):
#         h = (self.length**2 + self.width**2)**0.5
#         print("Гипотенуза прямоугольника:", round(h, 2))
#
#     def print_rectangle(self):
#         for x in range(self.length):
#             for y in range(self.width):
#                 print("*", end='')
#             print()
#
#
# r = Rectangle(3, 9)
# r.s_rectangle()
# r.rectangle_perimeter()
# r.rectangle_hypotenuse()
# r.print_rectangle()

# 03.03.23

import math

class Sphere:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def get_volume(self):
        return 4 / 3 * math.pi * self.r ** 3

    def get_square(self):
        return 4 * math.pi * self.r ** 2

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2 <= self.r ** 2


s = Sphere(0, 0, 6, 0.6)

print("get_radius:", s.get_radius())
print("get_volume:", s.get_volume())
print("get_square:", s.get_square())
print("get_center:", s.get_center())
print("get_square:", s.get_square())
print("is_point_inside (6, -1.5, 0):", s.is_point_inside(6, -1.5, 0))


s.set_radius(1.6)
print("set_radius (1.6):", s.get_radius())
print("is_point_inside (6, -1.5, 0):", s.is_point_inside(6, -1.5, 0))
