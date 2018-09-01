__author__ = 'Мишин Егор Олегович'
'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import randint

list_1 = [randint(1, 100) for _ in range(1, 20)]
maximum = list_1[0]
minimum = list_1[0]
max_index = 0
min_index = 0

print(f'Исходный список: {list_1}')
for i, item in enumerate(list_1):
    if item > maximum:
        maximum = item
        max_index = i
    if item < minimum:
        minimum = item
        min_index = i

print(f'\nmax = {maximum} max_index = {max_index}\n min = {minimum} min_index = {min_index}')
list_1[max_index], list_1[min_index] = list_1[min_index], list_1[max_index]
print(f'\nИзмененный список: {list_1}')
