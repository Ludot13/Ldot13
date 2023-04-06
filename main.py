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

# 17.02.23
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

# import math
#
# class Sphere:
#     def __init__(self, x, y, z, r):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.r = r
#
#     def get_volume(self):
#         return 4 / 3 * math.pi * self.r ** 3
#
#     def get_square(self):
#         return 4 * math.pi * self.r ** 2
#
#     def get_radius(self):
#         return self.r
#
#     def get_center(self):
#         return (self.x, self.y, self.z)
#
#     def set_radius(self, r):
#         self.r = r
#
#     def set_center(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def is_point_inside(self, x, y, z):
#         return (x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2 <= self.r ** 2
#
#
# s = Sphere(0, 0, 6, 0.6)
#
# print("get_radius:", s.get_radius())
# print("get_volume:", s.get_volume())
# print("get_square:", s.get_square())
# print("get_center:", s.get_center())
# print("get_square:", s.get_square())
# print("is_point_inside (6, -1.5, 0):", s.is_point_inside(6, -1.5, 0))
#
#
# s.set_radius(1.6)
# print("set_radius (1.6):", s.get_radius())
# print("is_point_inside (6, -1.5, 0):", s.is_point_inside(6, -1.5, 0))

# 10.03.23

# Variant 1
# class Account:
#     def __init__(self, balance):
#         self._balance = balance
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative")
#         self._balance = value

# Variant 2
# class Account:
#     def __init__(self, balance):
#         self._balance = balance
#
#     def get_balance(self):
#         return self._balance
#
#     def set_balance(self, value):
#         if value < 0:
#             raise ValueError("Balance can't be negative")
#         self._balance = value
#
#     balance = property(get_balance, set_balance)

# 12.03.23

# import math
# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def set_numbers(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_sum(self):
#         return self.a + self.b
#
#     def get_product(self):
#         return self.a * self.b
#
# class RightTriangle(Pair):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         self.c = math.sqrt(a**2 + b**2)
#
#     def get_hypotenuse(self):
#         return self.c
#
#     def get_area(self):
#         return self.a * self.b / 2
#
#     def print_info(self):
#         print(f"Прямоугольный треугольник ABC ({self.a}, {self.b}, {self.c:.2f})")
#         print(f"Площадь ABC: {self.get_area():.1f}")
#
# # создание объекта Pair
# p = Pair(5, 8)
# print(f"Сумма: {p.get_sum()}")
# print(f"Произведение: {p.get_product()}")
#
# # изменение объекта Pair
# p.set_numbers(10, 20)
# print(f"Сумма: {p.get_sum()}")
# print(f"Произведение: {p.get_product()}")
#
# # создание объекта RightTriangle
# t = RightTriangle(5, 8)
# print(f"Гипотенуза ABC: {t.get_hypotenuse():.2f}")
# t.print_info()
#
# # изменение объекта RightTriangle
# t.set_numbers(10, 20)
# print(f"Гипотенуза ABC: {t.get_hypotenuse():.2f}")
# print(f"Сумма: {t.get_sum()}")
# print(f"Произведение: {t.get_product()}")
# t.print_info()

# 17.03.23

# class Student:
#     def __init__(self, name, laptop):
#         self.name = name
#         self.laptop = laptop
#
#     def print_info(self):
#         print(f"Student name: {self.name}")
#         print(f"Laptop model: {self.laptop.model}")
#         print(f"Laptop processor: {self.laptop.processor}")
#         print(f"Laptop memory: {self.laptop.memory}")
#
#     class Laptop:
#         def __init__(self, model, processor, memory):
#             self.model = model
#             self.processor = processor
#             self.memory = memory
#
# roman_laptop = Student.Laptop("HP", "i7", 16)
# roman = Student("Roman", roman_laptop)
# roman.print_info()
#
# vladimir_laptop = Student.Laptop("HP", "i7", 16)
# vladimir = Student("Vladimir", vladimir_laptop)
# vladimir.print_info()
#
# -----------------------


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.notebook = self.Notebook()
#
#     def print_info(self):
#         print(f"Student name: {self.name}")
#         print(f"Notebook model: {self.notebook.model}")
#         print(f"Notebook processor: {self.notebook.processor}")
#         print(f"Notebook memory: {self.notebook.memory}")
#
#     class Notebook:
#         def __init__(self, model="Unknown", processor="Unknown", memory="Unknown"):
#             self.model = model
#             self.processor = processor
#             self.memory = memory
#
# # создаю объект класса Student
# student = Student("John")
#
# # устанавливаю информацию о ноутбуке
# student.notebook.model = "HP EliteBook"
# student.notebook.processor = "Intel Core i5-10310U"
# student.notebook.memory = "8 GB"
#
# # вывожу информацию о студенте и его ноутбуке
# student.print_info()

# 17.03.23
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end= " ")
#         self.note.show()
#
#     class Notebook:
#             def __init__(self):
#                 self.brand = 'HP'
#                 self.cpu = 'i7'
#                 self.ram = 16
#
#             def show(self):
#                 print(f" => {self.brand}, {self.cpu}, {self.ram}")
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
# s3 = Student("Sergey")
#
# s1.show()
# s2.show()
# s3.show()

# 19.03.23

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec % other.sec)
#
#
# c1 = Clock(600)
# c2 = Clock(200)
# c3 = c1 - c2
# print("c1:", c1.get_format_time())
# print("c1 - c2:", c3.get_format_time())
# c3 = c1 * c2
# print("c1 * c2:", c3.get_format_time())
# c3 = c1 // c2
# print("c1 // c2:", c3.get_format_time())
# c3 = c1 % c2
# print("c1 % c2:", c3.get_format_time())
# c1 -= c2
# print("c1 -= c2:", c1.get_format_time())
# c1 *= c2
# print("c1 *= c2:", c1.get_format_time())
# c1 //= c2
# print("c1 //= c2:", c1.get_format_time())
# c1 %= c2
# print("c1 %= c2:", c1.get_format_time())

# 24.03.23

# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __repr__(self):
#         return f"{self.x}, {self.y}, {self.z}"
# def __add__(self, other):
#     return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
# def __sub__(self, other):
#     return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
#
# def __mul__(self, other):
#     return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)
#
# def __truediv__(self, other):
#     return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)
#
# def __eq__(self, other):
#     return self.x == other.x and self.y == other.y and self.z == other.z
#
# def __str__(self):
#     return "({}, {}, {})".format(self.x, self.y, self.z)
#
# def __getitem__(self, key):
#     if key == "x":
#         return self.x
#     elif key == "y":
#         return self.y
#     elif key == "z":
#         return self.z
#
# def __setitem__(self, key, value):
#     if key == "x":
#         self.x = value
#     elif key == "y":
#         self.y = value
#     elif key == "z":
#         self.z = value
#
# p1 = Point3D(12, 15, 18)
# # p2 = Point3D(6, 3, 9)
# # print("Координаты 1-й точки:", p1)
# # print("Координаты 2-й точки:", p2)
# # p3 = p1 + p2
# # print("Сложение координат:", p3)
# # p3 = p1 - p2
# # print("Вычитание координат:", p3)
# # p3 = p1 * p2
# # print("Умножение:", p3)
# # p3 = p1 / p2
# # print("Деление:", p3)
# # if p1 == p2:
# #     print("Равенство координат: True")
# # else:
# #     print("Равенство координат: False")
# # print("x =", p1["x"], "x1 =", p2["x"])
# # print("y =", p1["y"], "y1 =", p2["y"])
# # print("z =", p1["z"], "z1 =", p2["z"])
# # p1["x"] = 20
# # print("Запись значения в координату x:", p1["x"])

# 24.03.23

# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __repr__(self):
#         return f"{self.x}, {self.y}, {self.z}"
#
#     def __add__(self, other):
#         return self.x + other.x, self.y + other.y, self.z + other.z
#
#     def __sub__(self, other):
#         return self.x - other.x, self.y - other.y, self.z - other.z
#
#     def __mul__(self, other):
#         return self.x * other.x, self.y * other.y, self.z * other.z
#
#     def __truediv__(self, other):
#         return self.x / other.x, self.y / other.y, self.z / other.z
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y and self.z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "x":
#             return self.x
#         elif item == "y":
#             return self.y
#         elif item == "z":
#             return self.z
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int or float):
#             raise ValueError("Значение должно быть числом")
#
#         if key == "x":
#             self.x = value
#
#         if key == "y":
#             self.y = value
#
#         if key == "z":
#             self.z = value
#
#
# p1 = Point3D(12, 15, 18)
# p2 = Point3D(6, 3, 9)
# print("Координаты 1-й точки:", p1)
# print("Координаты 2-й точки:", p2)
# p3 = p1 + p2
# print("Сложение координат:", p3)
# p3 = p1 - p2
# print("Вычитание координат:", p3)
# p3 = p1 * p2
# print("Умножение:", p3)
# p3 = p1 / p2
# print("Деление:", p3)
# if p1 == p2:
#     print("Равенство координат: True")
# else:
#     print("Равенство координат: False")
# print("x =", p1["x"], "x1 =", p2["x"])
# print("y =", p1["y"], "y1 =", p2["y"])
# print("z =", p1["z"], "z1 =", p2["z"])
# p1["x"] = 20
# print("Запись значения в координату x:", p1["x"])

# 26.03.23
# from abc import ABC, abstractmethod
# from math import sqrt
#
#
# class Shape(ABC):
#     def __init__(self, col):
#         self.col = col
#
#     @abstractmethod
#     def __call__(self):
#         ...
#
#     @abstractmethod
#     def area(self):
#         print("Площадь: ", end="")
#
#     @abstractmethod
#     def perimetr(self):
#         print("Периметр: ", end="")
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, s, col):
#         self.s = s
#         super().__init__(col)
#
#     def __call__(self):
#         print(f"===Квадрат===\nСторона: {self.s}\nЦвет: {self.col}")
#
#     def area(self):
#         super().area()
#         print(self.s ** 2)
#
#     def perimetr(self):
#         super().perimetr()
#         print(4 * self.s)
#
#     def draw(self):
#         for i in range(self.s):
#             print('*' * self.s)
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width, col):
#         self.length = length
#         self.width = width
#         super().__init__(col)
#
#     def __call__(self):
#         print(f"===Прямоугольник===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.col}")
#
#     def area(self):
#         super().area()
#         print(self.length * self.width)
#
#     def perimetr(self):
#         super().perimetr()
#         print((self.length + self.width)*2)
#
#     def draw(self):
#         for i in range(self.length):
#             print('*' * self.width)
#
#
# class Triangle(Shape):
#     def __init__(self, s1, s2, s3, col):
#         self.s1 = s1
#         self.s2 = s2
#         self.s3 = s3
#         super().__init__(col)
#
#     def __call__(self):
#         print(f"===Треугольник===\nСторона 1: {self.s1}\nСторона 2: {self.s2}\nСторона 3: {self.s3}\nЦвет: {self.col}")
#
#     def area(self):
#         super().area()
#         print(round((self.s1 / 4) * (sqrt(4 * self.s2 ** 2 - self.s1 ** 2)), 2))
#
#     def perimetr(self):
#         super().perimetr()
#         print(self.s1 + self.s2 + self.s3)
#
#     def draw(self):
#         for i in range(self.s2):
#             print(' ' * (self.s2 - 1 - i) + '*' * (1 + i * 2))
#
#
# p1 = Square(3, "red")
# p2 = Rectangle(3, 7, "green")
# p3 = Triangle(11, 6, 6, "yellow")
# px = [p1, p2, p3]
#
# for x in px:
#     x()
#     x.area()
#     x.perimetr()
#     x.draw()
#     print()
#     print()

# 31.03.23
# class Integer:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int) or value <= 0:
#             raise ValueError(f"Координата {value} должна быть целым, положительным числом")
#         instance.__dict__[self.name] = value
#
# class Triangle:
#     s1 = Integer()
#     s2 = Integer()
#     s3 = Integer()
#
#     def __init__(self, s1, s2, s3):
#         self.s1 = s1
#         self.s2 = s2
#         self.s3 = s3
#
#     def triangle_test(self):
#         if self.s1 + self.s2 > self.s3 and self.s1 + self.s3 > self.s2 and self.s2 + self.s3 > self.s1:
#             return f"Треугольник со сторонами {self.s1, self.s2, self.s3} существует."
#         else:
#             return f"Треугольник со сторонами {self.s1, self.s2, self.s3} не существует."
#
#
# p = Triangle(2, 5, 6)
# print(p.triangle_test())
# p = Triangle(5, 2, 8)
# print(p.triangle_test())
# p = Triangle(7, 3, 6)
# print(p.triangle_test())

# 02.04.23

# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def gen_key():
#     key = ''
#     nums = ['1', '2', 'n', '4', 'a', 't', '6']
#
#     while len(key) != 8:
#         key += choice(nums)
#     return key
#
#
# def write_json(person_dict, key_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = dict()
#
#     data[key_dict] = person_dict
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person(), gen_key())


# 07.04

# import json
#
# with open('countries.json', 'r') as f:
#     countries = json.load(f)
#
# delete_country = input("Введите название страны для удаления: ")
#
# if delete_country in countries:
#     del countries[delete_country]
#     with open('countries.json', 'w') as f:
#         json.dump(countries, f)
#     print("Данные успешно удалены")
# else:
#     print("Данные не найдены")
#
#
# import json
#
# with open('countries.json', 'r') as f:
#     countries = json.load(f)
#
# search_country = input("Введите название страны для поиска: ")
#
# if search_country in countries:
#     print(f"Страна: {search_country}, Столица: {countries[search_country]}")
# else:
#     print("Данные не найдены")
#
#
# import json
#
# with open('countries.json', 'r') as f:
#     countries = json.load(f)
#
# edit_country = input("Введите название страны для редактирования: ")
#
# if edit_country in countries:
#     print(f"Текущая столица: {countries[edit_country]}")
#     new_capital = input("Введите новое название столицы: ")
#     countries[edit_country] = new_capital
#     with open('countries.json', 'w') as f:
#         json.dump(countries, f)
#     print("Данные успешно отредактированы")
# else:
#     print("Данные не найдены")
#
#
# import json
#
# with open('countries.json', 'r') as f:
#     countries = json.load(f)
#
# for country, capital in countries.items():
#     print(f"Страна: {country}, Столица: {capital}")


# 07.04
# import json
#
# class Place:
#     data = dict()
#
#     def __call__(self):
#         print('*' * 30, "\nВыбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                         "4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы")
#
#     @staticmethod
#     def write_json(country_dict, city_dict):
#         data = json.load(open('country.json'))
#         data[country_dict] = city_dict
#         with open('country.json', 'w') as f:
#             json.dump(data, f, indent=2)
#         print("Файл сохранен")
#
#     @staticmethod
#     def delete_json(country_dict):
#         data = json.load(open('country.json'))
#         del data[country_dict]
#         with open('country.json', 'w') as f:
#             json.dump(data, f, indent=2)
#         print("Файл успешно отредактирован и сохранен")
#
#     @staticmethod
#     def search_json(country_dict):
#         data = json.load(open('country.json'))
#         if country_dict in data:
#             print(f"Страна: {country_dict}, со столицей: {data[country_dict]} хранится в нашей базе")
#         else:
#             print("Такая страна отсутствует в нашей базе")
#
#     @staticmethod
#     def redaction_json(country_dict, city_dict):
#         data = json.load(open('country.json'))
#         data[country_dict] = city_dict
#         with open('country.json', 'w') as f:
#             json.dump(data, f, indent=2)
#         print("Файл успешно отредактирован и сохранен")
#
#     @staticmethod
#     def info():
#         with open('country.json', 'r') as f:
#             data = json.load(f)
#             print(data)
#
#     def action(self, number):
#         while number != 6:
#             if number == 1:
#                 country1 = input("Введите название страны (с заглавной буквы): ")
#                 city1 = input("Введите название столицы (с заглавной буквы): ")
#                 self.write_json(country1, city1)
#                 self.__call__()
#                 self.action(int(input("Ввод: ")))
#             elif number == 2:
#                 country2 = input("Введите страну, которую хотите удалить (с заглавной буквы): ")
#                 self.delete_json(country2)
#                 self.__call__()
#                 self.action(int(input("Ввод: ")))
#             elif number == 3:
#                 country3 = input("Введите страну, которую хотите найти (с заглавной буквы): ")
#                 self.search_json(country3)
#                 self.__call__()
#                 self.action(int(input("Ввод: ")))
#             elif number == 4:
#                 country4 = input("Введите страну, которую хотите отредактировать (с заглавной буквы): ")
#                 city4 = input("Введите новое название столицы: ")
#                 self.redaction_json(country4, city4)
#                 self.__call__()
#                 self.action(int(input("Ввод: ")))
#             elif number == 5:
#                 self.info()
#                 self.__call__()
#                 self.action(int(input("Ввод: ")))
#             break
#
#
# s = Place()
# s()
# num = int(input("Ввод: "))
# s.action(num)
# print("Работа завершена")
# print(30 * '*')

# 09.04

# pip install beautifulsoup4 request

# from bs4 import BeautifulSoup


# import requests
# from bs4 import BeautifulSoup
# import csv
#
# def get_html(url):
#     response = requests.get(url)
#     if not response.ok:
#         print(f"Server responded with {response.status_code}")
#     else:
#         return response.text
#
#
# def parse_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     movie_list = soup.find_all('div', {'class': 'lister-item mode-advanced'})
#
#     data = []
#     for movie in movie_list:
#         title = movie.find('h3', {'class': 'lister-item-header'}).a.text.strip()
#         year = movie.find('span', {'class': 'lister-item-year'}).text.strip('()')
#         rating = movie.find('div', {'class': 'ratings-bar'}).strong.text.strip()
#         link = movie.find('h3', {'class': 'lister-item-header'}).a.get('href')
#         data.append([title, year, rating, link])
#
#     return data
#
# def write_csv(data):
#     with open('movies.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Title', 'Year', 'Rating', 'Link'])
#         writer.writerows(data)
#
# url = 'https://www.imdb.com/chart/top'
#
# html = get_html(url)
# data = parse_html(html)
# write_csv(data)

# import requests
# from bs4 import BeautifulSoup
# import csv
#
# url = 'https://www.imdb.com/chart/top/'
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# movies = soup.select('td.titleColumn')
# crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
# ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name="ir"]')]
#
# movie_data = []
#
# for i in range(len(movies)):
#     movie_string = movies[i].get_text()
#     movie = (' '.join(movie_string.split()).replace('.', ''), crew[i], ratings[i], 'https://www.imdb.com' + movies[i].a.attrs.get('href'))
#     movie_data.append(movie)
#
# headers = ['Title', 'Year/Crew', 'Rating', 'Link']
#
# with open('movies.csv', 'w', encoding='utf-8', newline='') as output_file:
#     writer = csv.writer(output_file)
#     writer.writerow(headers)
#     writer.writerows(movie_data)
#
# print('Parsing completed successfully. Check the movies.csv file for the results.')

# 14.04

import requests
from bs4 import BeautifulSoup
import csv


class IMDBScraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.ok:
            return response.text
        else:
            print('Error loading page', self.url)

    def parse_top_250(self):
        data = []
        html = self.fetch_data()
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('tbody', {'class': 'lister-list'})
        rows = table.find_all('tr')
        for row in rows:
            title_column = row.find('td', {'class': 'titleColumn'})
            title = title_column.a.text
            year = title_column.span.text.strip('()')
            rating = row.find('td', {'class': 'ratingColumn'}).strong.text
            data.append([title, year, rating])
        return data

    def parse_top_250_no_pandas(self):
        data = []
        html = self.fetch_data()
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('tbody', {'class': 'lister-list'})
        rows = table.find_all('tr')
        for row in rows:
            title_column = row.find('td', {'class': 'titleColumn'})
            title = title_column.a.text
            year = title_column.span.text.strip('()')
            rating = row.find('td', {'class': 'ratingColumn'}).strong.text
            data.append([title, year, rating])
        return data


url = 'https://www.imdb.com/chart/top/'
scraper = IMDBScraper(url)
data = scraper.parse_top_250()
for item in data:
    print(item)

# save data to a CSV file
with open('imdb_top_250.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Year', 'Rating'])
    writer.writerows(data)
print('Data saved to imdb_top_250.csv.')