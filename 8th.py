__author__ = 'Мишин Егор Олегович'
"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. 
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку. 
В конце следует вывести полученную матрицу.
"""


print('Заполнение матрицы:')
matrix = [[int(input(f'Введите элемент\nстрока - {value}, столбец - {value1}: '))
           for value in range(1, 5)] for value1 in range(1, 5)]

for row in matrix:
    summa = 0
    for i, value in enumerate(row):
        summa += value
    row.append(summa)


print('\nМатрица:')
for row in matrix:
    print(row)
