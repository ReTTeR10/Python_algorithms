__author__ = 'Мишин Егор Олегович'
"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


from random import randint

list_1 = [randint(1, 100) for _ in range(1, 20)]
maximum = list_1[0]
minimum = list_1[0]
max_index = 0
min_index = 0
summa = 0

print(f'Исходный список: {list_1}')
for i, item in enumerate(list_1):
    if item > maximum:
        maximum = item
        max_index = i
    if item < minimum:
        minimum = item
        min_index = i
if min_index > max_index:
    for i in list_1[max_index + 1:min_index]:
        summa += i
else:
    for i in list_1[min_index + 1:max_index]:
        summa += i


print(f'\nМаксимальный элемент = {maximum} позиция = {max_index}'
      f'\nМинимальный элемент = {minimum} позиция = {min_index}'
      f'\nСумма элементов между ними = {summa}')
