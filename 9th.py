__author__ = 'Мишин Егор Олегович'
"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import randint

list_min = []
lenth = int(input('Введите количество столбцов матрицы'))
high = int(input('Введите количество строк матрицы'))

matrix = [[randint(-9, 9) for _ in range(lenth)]for _ in range(high)]

print('\nНаша матрица:')
for row in matrix:
    print(row)

new_matrix = list(map(list, zip(*matrix)))
'''
транспонируем матрицу чтобы найти минимальный элемент в столбце, так как
т.к. при транспонировании столбцы становятся строками, и искать удобнее
'''

for row in new_matrix:    # ищем минимальный элемент в строке(бывшем столбце)
    min_el = new_matrix[0][0]
    for item in row:
        if item < min_el:
            min_el = item
    list_min.append(min_el)    # добавляем в список


print(f'\nСписок минимальных элементов столбцов {list_min}')
max_el = list_min[0]
for item in list_min:
    if item > max_el:
        max_el = item

print(f'\nМаксимальный элемент среди минимальных элементов столбцов матрицы: {max_el}')
