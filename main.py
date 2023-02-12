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
def CalcSumNegativeNumbers(A):
    if A == []:
        return 0
    else:
        count = CalcSumNegativeNumbers(A[1:])
    if A[0]<0:
            count = count + 1
    return count

S = [ -2, 3, 8, -11, -4, 6 ]
n = CalcSumNegativeNumbers(L)
print("n = ", n)