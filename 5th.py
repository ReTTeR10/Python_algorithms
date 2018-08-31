__author__ = 'Мишин Егор Олегович'
"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import randint

list_1 = [randint(-9, 9) for _ in range(1, 20)]

max_el = -10
max_num = []
count = 0

for value in list_1:

    if value < 0 and value > max_el:
        max_el = value
for i, value in enumerate(list_1):      # пытался реализовать подсчет максимальных элементов в одином цикле с программой
    if value == max_el:                 # но не получилось
        count += 1
        max_num.append(i)


print(f'Наш список: {list_1}')
print(f'Максимальный отрицательный элемент: {max_el}, его позиция: {max_num}, встречается {count} раз')

